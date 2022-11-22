"""
Module containing the "Enemy" class.
"""

from ursina import Entity, Vec3, color, distance_xz, destroy, raycast, time

from .health_bar import HealthBar
from src.players.player import Player


class Enemy(Entity):
    """
    Class to represent an enemy.
    """
    player: Player

    def __init__(self, parent: Entity, player: Player, x_position: int) -> None:
        """
        Constructor to setup the Enemy.
        """
        self._set_enemy(parent, x_position)
        self._set_health()
        self._set_health_bar()

        self.player = player

    def update(self) -> None:
        """
        Method to update the enemy.

        This method is called on each frame.
        """
        player_is_too_far = self._is_player_too_far()

        if player_is_too_far:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)

        self.look_at_2d(self.player.position, "y")

        self._move_closer_to_player()

    def take_damage(self) -> None:
        """
        Method to receive the damage.
        """
        self.current_health -= 10

        if self.current_health <= 0:
            self._die()

        self._update_health_bar()

    def _die(self) -> None:
        """
        Method to kill the enemy.
        """
        destroy(self)

    def _update_health_bar(self) -> None:
        """
        Method to update the health bar.
        """
        self.health_bar.world_scale_x = self.current_health / self.max_health * 1.5
        self.health_bar.alpha = 1

    def _set_enemy(self, parent: Entity, x_position: int) -> None:
        """
        Private Method to set the enemy entity.
        """
        enemy_attributes = {
            "parent": parent,
            "model": "cube",
            "scale_y": 2,
            "origin_y": -0.5,
            "color": color.light_gray,
            "collider": "box",
            "x": x_position,
            "speed": 2
        }

        super().__init__(**enemy_attributes)

    def _set_health(self) -> None:
        """
        Private Method to set the enemy health.
        """
        self.max_health = self.current_health = 100

    def _set_health_bar(self) -> None:
        """
        Private Method to set the enemy health bar.
        """
        self.health_bar = HealthBar(self)

    def _move_closer_to_player(self) -> None:
        """"""
        hit_info = raycast(self.world_position + Vec3(0, 1, 0), self.forward, 30, ignore=(self,))

        if hit_info.entity != self.player:
            return

        distance_from_player = distance_xz(self.player.position, self.position)
        if distance_from_player <  2:
            return

        self.position += self.forward * time.dt * 5

    def _is_player_too_far(self) -> None:
        """
        Private Method to check whether the player is too far or not.
        """
        MAX_PLAYER_DISTANCE = 20

        distance_to_player = distance_xz(self.player.position, self.position)

        return distance_to_player > MAX_PLAYER_DISTANCE

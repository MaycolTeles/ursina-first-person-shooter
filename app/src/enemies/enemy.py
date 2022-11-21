"""
Module containing the "Enemy" class.
"""

from ursina import Entity, color, distance_xz, time

from .health_bar import HealthBar
from run import player


class Enemy(Entity):
    """
    Class to represent an enemy.
    """

    def update(self) -> None:
        """
        Method to update the enemy.

        This method is called on each frame.
        """
        player_is_too_far = self._is_player_too_far()

        if player_is_too_far:
            return

        self.health_bar.alpha = max(0, self.health_bar.alpha - time.dt)
        self.look_at_2d()

    def __init__(self) -> None:
        """
        Constructor to setup the Enemy.
        """
        self._set_enemy()
        self._set_health()
        self._set_health_bar()

    def _set_enemy(self) -> None:
        """
        Private Method to set the enemy entity.
        """
        enemy_attributes = {
            "parent": "PARENT",
            "model": "cube",
            "scale_y": 2,
            "origin_y": -0.5,
            "color": color.light_gray,
            "collider": "box"
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

    def _is_player_too_far(self) -> None:
        """
        Private Method to check whether the player is too far or not.
        """
        MAX_PLAYER_DISTANCE = 40

        distance_to_player = distance_xz(player.position, self.position)

        return distance_to_player > MAX_PLAYER_DISTANCE

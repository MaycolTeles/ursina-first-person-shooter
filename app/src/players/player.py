"""
Module containing the "Player" class.
"""

from ursina import BoxCollider, Vec3, color, held_keys
from ursina.prefabs.first_person_controller import FirstPersonController

from src.guns.gun import Gun


class Player(FirstPersonController):
    """
    Class to represent a player.
    """

    def update(self) -> None:
        """
        Method to update the player.

        This method is executed on each frame.
        """
        super().update()

        if held_keys['left mouse']:
            self.gun.shoot()

    def __init__(self) -> None:
        """
        Constructor to setup the Player.
        """
        self._set_player()
        self._set_collider()
        self._set_gun()

    def _set_player(self) -> None:
        """
        Private Method to set the player entity.
        """
        player_attributes = {
            "model": "cube",
            "z": -10,
            "color": color.orange,
            "origin_y": -0.5,
            "speed": 8
        }

        super().__init__(**player_attributes)

    def _set_collider(self) -> None:
        """
        Private Method to set the player's collider.
        """
        self.collider = BoxCollider(self, Vec3(0, 1, 0), Vec3(1, 2, 1))

    def _set_gun(self) -> None:
        """
        Private Method to set the player gun.
        """
        self.gun = Gun(self)

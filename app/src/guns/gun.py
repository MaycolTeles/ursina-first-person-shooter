"""
Module containing the "Gun" class.
"""

# TYPING IMPORTS
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.players.player import Player


# MODULE IMPORTS
from ursina import Entity, Vec3, color, invoke, mouse


class Gun(Entity):
    """
    Class to represent a gun.
    """
    on_cooldown: bool

    def __init__(self, player: Player) -> None:
        """
        Constructor to setup the gun.
        """
        self._setup_gun(player)

    def shoot(self) -> None:
        """
        Method to use the gun to shoot.
        """
        if self.on_cooldown:
            self._remove_recoil()
            return

        invoke(self._set_recoil, delay=0.15)
        invoke(setattr, self, "on_cooldown", False, delay=0.15)

        if mouse.hovered_entity:
            mouse.hovered_entity.take_damage()
            mouse.hovered_entity.blink(color.red)

        self.on_cooldown = True

    def _setup_gun(self, player: Player) -> None:
        """
        Private Method to set the gun entity.
        """
        gun_attributes = {
            "model": "assets/ak47/ak47.obj",
            "texture": "shore",
            "parent": player.camera_pivot,
            "position": Vec3(0.7, -1, 1.5),
            "scale": 0.01,
            "origin_z": -0.5,
            "color": color.red,
            "on_cooldown": False
        }

        super().__init__(**gun_attributes)

    def _set_recoil(self) -> None:
        """
        Private method to set the gun recoil.
        """
        self.rotation_x -= 2

    def _remove_recoil(self) -> None:
        """
        Private method to remove the gun recoil.
        """
        self.rotation_x = 0
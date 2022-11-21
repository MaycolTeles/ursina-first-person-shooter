"""
Module containing the "Gun" class.
"""

from ursina import Entity, camera, color


class Gun(Entity):
    """
    Class to represent a gun.
    """

    def __init__(self) -> None:
        """
        Constructor to setup the gun.
        """
        self._setup_gun()

    def _setup_gun(self) -> None:
        """
        Method to create the gun entity.
        """
        gun_attributes = {
            "model": "cube",
            "parent": camera,
            "position": (0.5, -0.25, 0.25),
            "scale": (0.3, 0.2, 1),
            "origin_z": -0.5,
            "color": color.red,
            "on_cooldown": False
        }

        super().__init__(**gun_attributes)

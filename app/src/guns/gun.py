"""
Module containing the "Gun" class.
"""

from ursina import Entity, camera, color, invoke


class Gun(Entity):
    """
    Class to represent a gun.
    """
    on_cooldown: bool

    def shoot(self) -> None:
        """
        Method to use the gun to shoot.
        """
        if self.on_cooldown:
            print("GUN ON COOLDOWN. NOT SHOOTING...")
            return

        self.muzzle_flash.enabled = True

        invoke(self.muzzle_flash.disable, delay=0.05)
        invoke(setattr, self, "on_cooldown", False, delay=0.15)

        self.on_cooldown = True

    def __init__(self) -> None:
        """
        Constructor to setup the gun.
        """
        self._setup_gun()
        self._set_flash()

    def _setup_gun(self) -> None:
        """
        Private Method to set the gun entity.
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

    def _set_flash(self) -> None:
        """
        Private method to set the gun flash.
        """
        flash_attributes = {
            "parent": self,
            "z": 1,
            "world_scale": 0.5,
            "model": "quad",
            "color": color.yellow,
            "enabled": False
        }

        self.muzzle_flash = Entity(**flash_attributes)

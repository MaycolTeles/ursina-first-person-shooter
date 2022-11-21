"""
Module containing the "Sky" class.
"""

from ursina import Entity, Vec3
from ursina import Sky as UrsinaSky
from ursina import DirectionalLight as UrsinaSun


class Sky(Entity):
    """
    Class to represent the Sky.
    """

    def __init__(self) -> None:
        """
        Constructor to setup the sky.
        """
        self._set_sky()
        self._set_sun()
        
    def _set_sky(self) -> None:
        """
        Private Method to setup the sky entity.
        """
        self.sky = UrsinaSky()

    def _set_sun(self) -> None:
        """
        Private Method to setup the sun entity.
        """
        self.sun = UrsinaSun()
        self.sun.look_at(Vec3(1, -1, -1))

"""
Module containing the "World" class.
"""

from ursina import Entity

from .ground import Ground
from .sky import Sky
from .wall import Wall


class World(Entity):
    """
    Class to represent a world.
    """

    def __init__(self) -> None:
        """
        Constructor to setup the world.
        """
        self._set_ground()
        self._set_sky()
        self._set_walls()

    def _set_ground(self) -> None:
        """
        Private Method to setup the world ground.
        """
        self.ground = Ground()

    def _set_sky(self) -> None:
        """
        Private Method to setup the world sky.
        """
        self.sky = Sky()

    def _set_walls(self) -> None:
        """
        Private Method to setup the world walls.
        """
        NUMBER_OF_WALLS = 15

        for _ in range(NUMBER_OF_WALLS):
            Wall()

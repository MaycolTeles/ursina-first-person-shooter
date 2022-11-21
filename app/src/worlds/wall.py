"""
Module containing the "Wall" class.
"""

from ursina import Entity, color, random


class Wall(Entity):
    """
    Class to represent a wall.
    """

    def __init__(self) -> None:
        """
        Constructor to setup the Wall.
        """
        self._set_wall()

    def _set_wall(self) -> None:
        """
        Private Method to set the wall entity.
        """
        wall_attributes = {
            "model": "cube",
            "origin_y": -0.5,
            "scale": 2,
            "texture": "brick",
            "texture_scale": (1, 2),
            "x": random.uniform(-8, 8),
            "z": random.uniform(-8, 8) + 8,
            "collider": "box",
            "scale_y": random.uniform(2, 3),
            "color": color.hsv(0, 0, random.uniform(0.9, 1)),
        }

        super().__init__(**wall_attributes)

"""
Module containing the "World" class.
"""

from ursina import Entity


class World(Entity):
    """
    Class to represent the World.
    """

    def __init__(self) -> None:
        """
        Constructor to setup the world.
        """
        self._set_world()
        
    def _set_world(self) -> None:
        """
        Private Method to setup the world entity.
        """
        world_attributes = {
            "model": "plane",
            "collider": "box",
            "scale": 30,
            "texture": "grass",
            "texture_scale": (4,4)
        }

        super().__init__(**world_attributes)

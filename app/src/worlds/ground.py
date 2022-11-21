"""
Module containing the "Ground" class.
"""

from ursina import Entity


class Ground(Entity):
    """
    Class to represent the Ground.
    """

    def __init__(self) -> None:
        """
        Constructor to setup the ground.
        """
        self._set_ground()
        
    def _set_ground(self) -> None:
        """
        Private Method to setup the ground entity.
        """
        ground_attributes = {
            "model": "plane",
            "collider": "box",
            "scale": 30,
            "texture": "grass",
            "texture_scale": (4,4)
        }

        super().__init__(**ground_attributes)

"""
Module containing the "HealthBar" class.
"""

from ursina import Entity, color


class HealthBar(Entity):
    """
    Class to represent a health bar.
    """

    def __init__(self, entity: Entity) -> None:
        """
        Constructor to setup the HealthBar.

        Parameters
        ----------
        entity : Entity
            The entity that this health bar belongs to.
        """
        self._set_health_bar(entity)

    def _set_health_bar(self, entity: Entity) -> None:
        """
        Private Method to set the entity's health bar entity, based on the entity received as argument.

        Parameters
        ----------
        entity : Entity
            The entity that this health bar belongs to.
        """
        health_bar_attributes = {
            "parent": entity,
            "model": "cube",
            "y": 1.2,
            "color": color.red,
            "world_scale": (1.5, 0.1, 0.1)
        }

        super().__init__(**health_bar_attributes)

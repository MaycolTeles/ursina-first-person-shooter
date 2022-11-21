"""
Module containing the "Game" class.
"""

from ursina import Ursina, Entity, mouse, random
from ursina.shaders import lit_with_shadows_shader

from src.enemies.enemy import Enemy
from src.players.player import Player
from src.worlds.world import World


class Game:
    """
    Class to represent the game.
    """

    def start(self) -> None:
        """
        Method to start the game.
        """
        self._setup_game()
        self._create_game_entities()

        self.app.run()

    def _setup_game(self) -> None:
        """
        Private Method to set up the game.
        """
        random.seed(0)
        Entity.default_shader = lit_with_shadows_shader
        mouse.traverse_target = self.enemy

    def _create_game_entities(self) -> None:
        """
        Private Method to create all the entities needed for the game to start.
        """
        self.app = Ursina()
        self.player = Player()
        self.world = World()
        self.enemies = [Enemy() for _ in range(4)]

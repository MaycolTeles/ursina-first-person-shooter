"""
Module containing the "Game" class.
"""

from ursina import Ursina, EditorCamera, Entity, application, mouse, random, window
from ursina.shaders import lit_with_shadows_shader

from src.enemies.enemy import Enemy
from src.enemies.shootable import Shootable
from src.players.player import Player
from src.worlds.world import World


class Game():
    """
    Class to represent the game.
    """

    def start(self) -> None:
        """
        Method to start the game.
        """
        self._setup_game()
        self._create_game_entities()

        window.size = (1200, 1080)
        window.position=(2100, 100)

        self.ursina.run()

    def _setup_game(self) -> None:
        """
        Private Method to set up the game.
        """
        random.seed(0)
        Entity.default_shader = lit_with_shadows_shader

        self.shootable = Shootable()
        mouse.traverse_target = self.shootable

    def _create_game_entities(self) -> None:
        """
        Private Method to create all the entities needed for the game to start.
        """
        self.ursina = Ursina()
        self.pause_handler = Entity(ignore_paused=True, input=self._pause_input)
        self.editor_camera = EditorCamera(enabled=False, ignore_paused=True)
        self.player = Player()
        self.world = World()
        self.enemies = [Enemy(self.shootable, self.player, i*4) for i in range(10)]

    def _pause_input(self, key: str):
        if key != 'tab':    # press tab to toggle edit/play mode
            return

        self.editor_camera.enabled = not self.editor_camera.enabled

        self.player.visible_self = self.editor_camera.enabled
        self.player.cursor.enabled = not self.editor_camera.enabled
        # self.player.gun.enabled = not self.editor_camera.enabled
        mouse.locked = not self.editor_camera.enabled
        self.editor_camera.position = self.player.position

        application.paused = self.editor_camera.enabled

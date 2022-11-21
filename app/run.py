"""
Module to run the application.
"""

from ursina import Ursina

from src.player.player import Player
from src.world.world import World


def main() -> None:
    """
    Main function to run the application.
    """
    app = Ursina()

    player = Player()
    world = World()

    app.run()


if __name__ == "__main__":
    main()

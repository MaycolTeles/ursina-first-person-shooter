"""
Module to run the application.
"""

from src.game import Game


def main() -> None:
    """
    Main function to run the application.
    """
    game = Game()
    game.start()


if __name__ == "__main__":
    main()

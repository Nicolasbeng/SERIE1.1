import arcade

from constants import *  # noqa: F403
from gameview import GameView

def main() -> None:
    window = arcade.Window(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT, WINDOW_TITLE)  # noqa: F405
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()

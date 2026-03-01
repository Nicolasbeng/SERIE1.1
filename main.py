import arcade

from constants import *
from gameview import GameView

def main() -> None:
    # Create the (unique) Window, setup our GameView, and launch
    window = arcade.Window(MAX_WINDOW_WIDTH, MAX_WINDOW_HEIGHT, WINDOW_TITLE)
    game_view = GameView()
    window.show_view(game_view)
    arcade.run()

if __name__ == "__main__":
    main()

from textures import *

def grid_to_pixel(i: int) -> int :
    return  i*TILE_SIZE + (TILE_SIZE//2)

class GameView(arcade.View) :

    player: Final[arcade.Sprite]

    def __init__(self) -> None:

        self.player = arcade.Sprite(
            TEXTURE_PLAYER_IDLE_DOWN,
            scale=SCALE, center_x=grid_to_pixels(2), center_y=grid_to_pixels(2)
        )

def on_draw(self) -> None:

    arcade.draw_sprite(self.player)

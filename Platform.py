import arcade
from constant import *


class Platform(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.image_source = "./assets/platform.png"
        self.sprite = arcade.Sprite(self.image_source, CHARACTER_SCALING)
        self.sprite.center_x = SCREEN_WIDTH / 2
        self.sprite.center_y = SCREEN_HEIGHT / 4

import arcade
from constant import *


class Wall(arcade.Sprite):
    def __init__(self,image_source,center_x, center_y):
        super().__init__()
        self.image_source = image_source
        self.sprite = arcade.Sprite(self.image_source, TILE_SCALING)
        self.sprite.center_x = center_x
        self.sprite.center_y = center_y

import random

import arcade
from arcade.color import RED
from constant import *

class Ball:
    def __init__(self):
        self.sprite: arcade.Sprite = arcade.Sprite("./assets/egg.png", 0.05)# set ball position in the middle
        self.sprite.position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        # randomize sprite direction and speed
        self.sprite.change_x = 0
        self.sprite.change_y = BALL_SPEED


    def update(self):
        self.sprite.update()  # update the sprite
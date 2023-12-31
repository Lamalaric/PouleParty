import random

import arcade
from arcade.color import RED
from constant import *

class Ball:
    def __init__(self):
        self.sprite: arcade.Sprite = arcade.Sprite("./assets/egg.png", 0.05,
                                                   texture=arcade.load_texture("./Assets/egg.png",
                                                                               width=512,
                                                                               height=512,
                                                                               hit_box_algorithm="Simple")
                                                   )  # set ball position in the middle
        self.sprite.position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 -50
        # randomize sprite direction and speed
        self.sprite.change_x = 0
        self.sprite.change_y = BALL_SPEED
        self.damage = 1

    def modify_damage(self):
        self.damage = self.sprite.width // BALL_SCALE+1
        # print(self.damage)

    def update(self):
        self.sprite.update()  # update the sprite
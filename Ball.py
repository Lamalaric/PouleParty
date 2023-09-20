import random

import arcade
from arcade.color import RED

from main import SCREEN_WIDTH, SCREEN_HEIGHT


class Ball:
    def __init__(self):
        self.sprite: arcade.Sprite = arcade.Sprite("./assets/egg.png", 0.05)# set ball position in the middle
        self.sprite.position = SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2
        # randomize sprite direction and speed
        self.sprite.change_x = random.choice([-3, -2, 3, 2])
        self.sprite.change_y = random.choice([-3, -2, 3, 2])


    def on_update(self, delta_time: float):
        self.sprite.update()  # update the sprite

        # bounce the sprite either at the top or at the bottom
        if self.sprite.bottom <= 0:
            self.sprite.change_y *= -1
        elif self.sprite.top >= SCREEN_HEIGHT:
            self.sprite.change_y *= -1

        # check if the sprite has collided with a paddle
        '''collided_paddle = self.sprite.collides_with_list(self.paddles)
        if collided_paddle:
            # adjust sprite coordinates to simplify the game
            if collided_paddle[0] is self.left_player.paddle:
                self.sprite.left = self.left_player.paddle.right
            else:
                self.sprite.right = self.right_player.paddle.left

            # bounce the sprite from the paddle
            self.sprite.change_x *= -1

        # check if the sprite has exited the screen in either side and
        # end the game
        if self.sprite.right <= 0:
            self.end_game(self.right_player)
        elif self.sprite.left >= self.window.width:
            self.end_game(self.left_player)
        '''
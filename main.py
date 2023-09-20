"""
Platformer Game
"""
import arcade
from Ball import Ball

from Platform import Platform
from Wall import Wall
from constant import *


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.platform = None
        self.LeftWall = None
        self.RightWall = None
        self.TopWall = None
        self.Ball = None

        # Our physics engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Initialize Scene
        self.scene = arcade.Scene()

        self.platform = Platform()
        self.scene.add_sprite("Player", self.platform.sprite)

        self.LeftWall = Wall("./assets/lateral_wall.PNG", 0, SCREEN_HEIGHT / 2)
        self.RightWall = Wall("./assets/lateral_wall.PNG", SCREEN_WIDTH, SCREEN_HEIGHT / 2)
        self.TopWall = Wall("./assets/vertical_wall.PNG", SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.scene.add_sprite("Walls", self.LeftWall.sprite)
        self.scene.add_sprite("Walls", self.RightWall.sprite)
        self.scene.add_sprite("Walls", self.TopWall.sprite)

        self.Ball = Ball()
        self.scene.add_sprite("Walls", self.Ball.sprite)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.platform.sprite, self.scene.get_sprite_list("Walls")
        )

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our Scene
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.RIGHT or key == arcade.key.Q:
            self.platform.sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.D:
            self.platform.sprite.change_x = -PLAYER_MOVEMENT_SPEED
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.RIGHT or key == arcade.key.Q:
            self.platform.sprite.change_x = 0
        elif key == arcade.key.LEFT or key == arcade.key.D:
            self.platform.sprite.change_x = 0

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()
        #Vérifie s'il y a une collision balle - plateforme, pour faire rebondir la balle
        self.Ball.update()
        self.collisionBallWall()
        if self.collisionBallPlatform():
            self.Ball.sprite.change_y *= -1


    def collisionBetween(self, sprite1, sprite2):
        return sprite1.collides_with_sprite(sprite2)

    def collisionBallPlatform(self):
        if self.collisionBetween(self.platform.sprite, self.Ball.sprite):
            # self.platform. += 3
            return True
        return False
    def collisionBallWall(self):
        #Mur bas
        # if self.sprite.bottom <= 0:
        #     self.sprite.change_y *= -1
        #Mur haut
        if self.collisionBetween(self.TopWall.sprite, self.Ball.sprite):
            self.Ball.sprite.change_y *= -1
            return True
        #Mur gauche
        if self.collisionBetween(self.LeftWall.sprite, self.Ball.sprite):
            self.Ball.sprite.change_x *= -1
            return True
        #Mur droit
        elif self.collisionBetween(self.RightWall.sprite, self.Ball.sprite):
            self.Ball.sprite.change_x *= -1
            return True
        return False


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

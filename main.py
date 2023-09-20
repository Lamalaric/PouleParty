"""
Platformer Game
"""
import arcade
import Ball

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

        left_wall = Wall("./assets/lateral_wall.PNG", 0, SCREEN_HEIGHT / 2)
        self.scene.add_sprite("Walls", left_wall.sprite)

        right_wall = Wall("./assets/lateral_wall.PNG", SCREEN_WIDTH, SCREEN_HEIGHT / 2)
        self.scene.add_sprite("Walls", right_wall.sprite)

        right_wall = Wall("./assets/vertical_wall.PNG", SCREEN_WIDTH/2, SCREEN_HEIGHT)
        self.scene.add_sprite("Walls", right_wall.sprite)

        self.Ball = Ball.Ball()
        Ball.setup()

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


def main():
    """Main function"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

"""
Platformer Game
"""
import arcade
import Ball

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 0.2
EGG_SCALING = 0.05
TILE_SCALING = 2

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5


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
        self.player_sprite = None
        self.Ball = None

        # Our physics engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

        # Initialize Scene
        self.scene = arcade.Scene()

        # Set up the player, specifically placing it at these coordinates.
        image_source = "./assets/platform.png"
        self.player_sprite = arcade.Sprite(image_source, CHARACTER_SCALING)
        self.player_sprite.center_x = SCREEN_WIDTH/2
        self.player_sprite.center_y = SCREEN_HEIGHT/4
        self.scene.add_sprite("Player", self.player_sprite)

        # Create the ground
        left_wall = arcade.Sprite("./assets/lateral_wall.PNG", TILE_SCALING)
        left_wall.center_x = 0
        left_wall.center_y = SCREEN_HEIGHT/4
        self.scene.add_sprite("Walls", left_wall)

        right_wall = arcade.Sprite("./assets/lateral_wall.PNG", TILE_SCALING)
        right_wall.center_x = SCREEN_WIDTH
        right_wall.center_y = SCREEN_HEIGHT/4
        self.scene.add_sprite("Walls", right_wall)

        right_wall = arcade.Sprite("./assets/vertical_wall.PNG", TILE_SCALING)
        right_wall.center_x = SCREEN_WIDTH/2
        right_wall.center_y = SCREEN_HEIGHT
        self.scene.add_sprite("Walls", right_wall)


        self.Ball = Ball.Ball()
        Ball.setup()

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.scene.get_sprite_list("Walls")
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
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.D:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.RIGHT or key == arcade.key.Q:
            self.player_sprite.change_x = 0
        elif key == arcade.key.LEFT or key == arcade.key.D:
            self.player_sprite.change_x = 0


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
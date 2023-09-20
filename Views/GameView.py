import arcade
from constant import *
from Controllers.Wall import Wall
from Controllers.Platform import Platform


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.platform = None

        # Our physics engine
        self.physics_engine = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

    def on_show_view(self):

        # Initialize Scene
        self.scene = arcade.Scene()

        self.platform = Platform()
        self.scene.add_sprite("Player", self.platform.sprite)

        left_wall = Wall("./Assets/lateral_wall.PNG", 0, SCREEN_HEIGHT / 2)
        self.scene.add_sprite("Walls", left_wall.sprite)

        right_wall = Wall("./Assets/lateral_wall.PNG", SCREEN_WIDTH, SCREEN_HEIGHT / 2)
        self.scene.add_sprite("Walls", right_wall.sprite)

        right_wall = Wall("./Assets/vertical_wall.PNG", SCREEN_WIDTH / 2, SCREEN_HEIGHT)
        self.scene.add_sprite("Walls", right_wall.sprite)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.platform.sprite, self.scene.get_sprite_list("Walls")
        )

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Draw our Scene
        self.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.RIGHT or key == arcade.key.W:
            self.platform.move_right()
        elif key == arcade.key.LEFT or key == arcade.key.S:
            self.platform.move_left()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if (key == arcade.key.RIGHT or key == arcade.key.W) or (key == arcade.key.LEFT or key == arcade.key.S):
            self.platform.stop()

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

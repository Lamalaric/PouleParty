import arcade

from Controllers.Ball import Ball
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
        self.TopWall = None
        self.RightWall = None
        self.LeftWall = None
        self.Ball = None

        # Our physics engine
        self.physics_engine = None

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

    def on_show_view(self):

        # Initialize Scene
        self.scene = arcade.Scene()

        self.platform = Platform()
        self.scene.add_sprite("Player", self.platform.sprite)

        #Ajout murs
        self.LeftWall = Wall("./assets/lateral_wall.PNG", 0, SCREEN_HEIGHT / 2)
        self.RightWall = Wall("./assets/lateral_wall.PNG", SCREEN_WIDTH, SCREEN_HEIGHT / 2)
        self.TopWall = Wall("./assets/vertical_wall.PNG", SCREEN_WIDTH / 2, SCREEN_HEIGHT)
        self.scene.add_sprite("Walls", self.LeftWall.sprite)
        self.scene.add_sprite("Walls", self.RightWall.sprite)
        self.scene.add_sprite("Walls", self.TopWall.sprite)
        #Ajout balle
        self.Ball = Ball()
        self.scene.add_sprite("Walls", self.Ball.sprite)

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
        # Vérifie s'il y a une collision balle - plateforme, pour faire rebondir la balle
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
        # Mur bas
        # if self.Ball.sprite.bottom <= 0:
        #     gameover_view = GameOverView()
        #     self.window.show_view(gameover_view)
        # Mur haut
        if self.collisionBetween(self.TopWall.sprite, self.Ball.sprite):
            self.Ball.sprite.change_y *= -1
            return True
        # Mur gauche
        if self.collisionBetween(self.LeftWall.sprite, self.Ball.sprite):
            self.Ball.sprite.change_x *= -1
            return True
        # Mur droit
        elif self.collisionBetween(self.RightWall.sprite, self.Ball.sprite):
            self.Ball.sprite.change_x *= -1
            return True
        return False
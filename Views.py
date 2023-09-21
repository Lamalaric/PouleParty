import arcade
import random
from Controllers.Wall import Wall
from Controllers.Ball import Ball
from Controllers.Platform import Platform
from constant import *


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background = None

    def on_show_view(self):
        self.background = arcade.load_texture("./Assets/maxresdefault.png")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        arcade.draw_text("Poule Party", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,
                         arcade.color.WHITE, font_size=50, anchor_x="center")
        arcade.draw_text("Click to advance", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75,
                         arcade.color.WHITE, font_size=20, anchor_x="center")

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", SCREEN_WIDTH/2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 54,anchor_x="center")
        arcade.draw_text("Click to restart", SCREEN_WIDTH/2, SCREEN_HEIGHT / 2 - 75, arcade.color.WHITE, 24,anchor_x="center")

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        #output_total = f"Total Score: {self.window.total_score}"
        #arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__()

        # Our Scene Object
        self.scene = None
        self.sound = arcade.Sound("./Assets/Chicken Techno_8410qUT4QtA.mp3", streaming=False)
        self.media_player = self.sound.play(pan=0.5, volume=0.5,loop=True)
        self.background = None
        # Separate variable that holds the player sprite
        self.platform = None
        self.TopWall = None
        self.RightWall = None
        self.LeftWall = None
        self.Ball = None

        # Our physics engine
        self.physics_engine = None
        self.left_key = False
        self.right_key = False

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

    def on_show_view(self):

        # Initialize Scene
        self.scene = arcade.Scene()

        self.platform = Platform()
        self.scene.add_sprite("Player", self.platform.sprite)

        # Ajout murs
        self.LeftWall = Wall("./assets/murV2.png", 0, SCREEN_HEIGHT / 2)
        self.RightWall = Wall("./assets/murV2.png", SCREEN_WIDTH, SCREEN_HEIGHT / 2)
        self.TopWall = Wall("./assets/murH2.png", SCREEN_WIDTH / 2, SCREEN_HEIGHT)

        self.scene.add_sprite("Walls", self.LeftWall.sprite)
        self.scene.add_sprite("Walls", self.RightWall.sprite)
        self.scene.add_sprite("Walls", self.TopWall.sprite)

        # Ajout balle
        self.Ball = Ball()
        self.scene.add_sprite("Walls", self.Ball.sprite)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.platform.sprite, self.scene.get_sprite_list("Walls")
        )

        self.background = arcade.load_texture("./Assets/fond_jeu.jpg")

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        # Draw our Scene
        self.scene.draw()


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.RIGHT or key == arcade.key.W:
            self.right_key = True
            self.platform.move_right()
        elif key == arcade.key.LEFT or key == arcade.key.S:
            self.left_key = True
            self.platform.move_left()
    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""
        if key == arcade.key.RIGHT or key == arcade.key.W:
            self.right_key = False
            if self.left_key:
                self.platform.move_left()
            else:
                self.platform.stop()
        if key == arcade.key.LEFT or key == arcade.key.S:
            self.left_key = False
            if self.right_key:
                self.platform.move_right()
            else:
                self.platform.stop()

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()
        self.Ball.update()
        # Corrige le bug de plateforme qui tombe en la remontant
        if self.platform.toMoveUpward:
            self.platform.moveUpward()

        # Vérifie la collision balle - mur pour rebondir
        self.collisionBallWall()
        # Vérifie s'il y a une collision balle - plateforme, pour faire rebondir la balle d'un angle X random
        if self.collisionBallPlatform():
            self.platform.toMoveUpward = True
            self.Ball.sprite.change_x = self.setRandomBallForce()
            self.Ball.sprite.change_y *= -1
            '''
            # Détection si y'a triche
            if self.hasBallTouchedSides(self.platform, self.Ball):
                print('TRICHEUR')
            '''

    def collisionBetween(self, sprite1, sprite2):
        return sprite1.collides_with_sprite(sprite2)
    def collisionBallPlatform(self):
        if self.collisionBetween(self.platform.sprite, self.Ball.sprite):
            # self.platform. += 3
            return True
        return False
    def collisionBallWall(self):
        # Mur bas
        if self.Ball.sprite.bottom <= 0:
            game_over_view = GameOverView()
            self.window.show_view(game_over_view)
            self.sound.stop(self.media_player)
            # ViewManager.display_game_over(self.window)
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

    def setRandomBallForce(self):
        return random.randint(-6, 6)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """
        # Récupère le sprite cliqués
        # cards = arcade.get_sprites_at_point((x, y), *sprite list des blocks*)

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        theta = scroll_y * 2
        print(theta)
        self.platform.angle += theta

    '''
    def hasBallTouchedSides(self, platform, ball):
        platformY = platform.get_hit_box()
        print(platformY)
        return False
    '''
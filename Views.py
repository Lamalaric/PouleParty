import arcade
import random
from Controllers.Level import Level
from Controllers.Wall import Wall
from Controllers.Ball import Ball
from Controllers.Platform import Platform
from constant import *


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.background = None

    def on_show_view(self):
        self.background = arcade.load_texture("./Assets/menuStart.png")

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView(Level(1, "./Assets/fond_jeu.jpg"))
        self.window.show_view(game_view)


class GameOverView(arcade.View):
    def __init__(self, timer, score):
        super().__init__()
        self.timer_text = arcade.Text(
            text="00:00:00",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT // 2 - 50,
            color=arcade.color.WHITE,
            font_size=100,
            anchor_x="center",
        )
        self.timer = timer
        self.score = score

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 54, anchor_x="center")
        arcade.draw_text("Click to restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75, arcade.color.WHITE, 24,
                         anchor_x="center")

        # timer
        # Calculate minutes
        minutes = int(self.timer) // 60

        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.timer) % 60

        # Calculate 100s of a second
        seconds_100s = int((self.timer - seconds) * 100)

        # Use string formatting to create a new text string for our timer
        self.timer_text.text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"

        # time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {self.timer_text.text}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        arcade.draw_text(f"Score : {self.score}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 100,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        # output_total = f"Total Score: {self.window.total_score}"
        # arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView(Level(1, "./Assets/fond_jeu.jpg"))
        self.window.show_view(game_view)


class GameView(arcade.View):
    """
    Main application class.
    """

    def __init__(self, level):

        # Call the parent class and set up the window
        super().__init__()

        # Our Scene Object
        self.effect_player = None
        self.effect_music = None
        self.bricks = None
        self.scene = None
        self.background_music = arcade.Sound("./Assets/Run-Amok(chosic.com).mp3", streaming=False)
        self.media_player = self.background_music.play(pan=0.5, volume=0.5, loop=True)
        self.background = None
        # Separate variable that holds the player sprite
        self.platform = None
        self.TopWall = None
        self.RightWall = None
        self.LeftWall = None
        self.Ball = None
        self.level = level

        # Our physics engine
        self.physics_engine = None
        self.left_key = False
        self.right_key = False

        # score, vie et timer
        self.time_taken = 0
        self.time_text = arcade.Text(
            text="00:00:00",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT // 2 - 50,
            color=arcade.color.WHITE,
            font_size=100,
            anchor_x="center",
        )
        self.levelText = arcade.Text(
            text=f"{self.level.levelNumber}",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT // 2 - 50,
            color=arcade.color.WHITE,
            font_size=100,
            anchor_x="center",
        )
        self.score = 0
        self.vie = 3
        self.wait = False

    def setup(self):
        """Set up the game here. Call this function to restart the game."""

    def on_show_view(self):
        # Affiche le niveau actuel
        self.levelText.text = f"{self.level.levelNumber}"

        # Initialize Scene
        self.scene = arcade.Scene()

        # Ajout player
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
        self.scene.add_sprite("Ball", self.Ball.sprite)

        # self.background = arcade.load_texture("./Assets/fond_jeu.jpg")
        self.background = arcade.load_texture(self.level.background)

        bricksLeft = arcade.SpriteList()
        for brickline in self.level.brickLines:
            for brick in brickline:
                mySprite = brick.sprite
                mySprite.guid = f"Brick-{brick.id}"

                bricksLeft.append(mySprite)
                self.scene.add_sprite("Bricks", mySprite)
                # self.scene.add_sprite(f"Brick-{brick.id}", brick.sprite)
                # self.scene.add_sprite_list("Bricks", mySprite)
                print(f"Brick-{brick.id}")

    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        arcade.draw_lrwh_rectangle_textured(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.wait:
            pass
            # arcade.draw_text("Click to continue", SCREEN_WIDTH / 2 , SCREEN_HEIGHT / 2 +100, arcade.color.BLACK, 24)

        # Draw our Scene
        self.scene.draw()

        # score, vie et timer
        arcade.draw_text(f"Score : {self.score}",
                         SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT - 80,
                         arcade.color.BLACK,
                         font_size=15,
                         anchor_x="center")

        # Calculate minutes
        minutes = int(self.time_taken) // 60
        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.time_taken) % 60
        # Calculate 100s of a second
        seconds_100s = int((self.time_taken - seconds) * 100)
        # Use string formatting to create a new text string for our timer
        self.time_text.text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"
        # time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time : {self.time_text.text}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 80,
                         arcade.color.BLACK,
                         font_size=15,
                         anchor_x="center")
        arcade.draw_text(f"Life : {self.vie}",
                         3 * SCREEN_WIDTH / 4,
                         SCREEN_HEIGHT - 80,
                         arcade.color.BLACK,
                         font_size=15,
                         anchor_x="center")

        arcade.draw_text(f"{self.levelText.text}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 40,
                         arcade.color.BLACK,
                         font_size=24,
                         anchor_x="center")

    def on_update(self, delta_time):
        """Movement and game logic"""
        self.Ball.update()
        if not self.wait:
            # Déplacement de la balle
            # self.Ball.update()

            # Corrige le bug de plateforme qui tombe en la remontant
            if self.platform.toMoveUpward:
                self.platform.moveUpward()

            # Vérifie la collision balle - mur pour rebondir
            self.collisionBallWall()

            # Vérifie s'il y a une collision balle - plateforme, pour faire rebondir la balle d'un angle X random
            if self.collisionBallPlatform():
                self.platform.toMoveUpward = True
                self.Ball.sprite.change_x = (self.Ball.sprite.center_x - self.platform.sprite.center_x) / 10
                self.Ball.sprite.change_y *= -1
            # Vérifie la collision balle - brique
            if self.collisionBallBricks():
                self.score += 5

            # Accumulate the total time
            self.time_taken += delta_time

            # winning
            if len(self.scene["Bricks"]) == 0:
                game_won_view = GameWinView(self.time_taken, self.score, self.level)
                self.window.show_view(game_won_view)

    def collisionBetween(self, sprite1, sprite2):
        return sprite1.collides_with_sprite(sprite2)

    def collisionBallPlatform(self):
        if self.collisionBetween(self.platform.sprite, self.Ball.sprite):
            self.effect_music = arcade.Sound("./Assets/bonk-sound-effect-36055.mp3", streaming=False)
            self.effect_player = self.effect_music.play(pan=0.5, volume=0.4, loop=False)
            # self.platform. += 3
            return True
        return False

    def collisionBallWall(self):
        # Mur bas
        if self.Ball.sprite.bottom <= 0:
            if self.vie == 1:
                self.endGame()
            else:
                self.loseLife()
                return True

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

    def collisionBallBricks(self):
        bricksTouched = arcade.check_for_collision_with_list(self.Ball.sprite, self.scene["Bricks"])
        if len(bricksTouched) > 0:
            print(self.Ball.damage)
            self.Ball.sprite.change_y *= -1
            for brick in bricksTouched:
                touchedBrick = self.level.getBrickById(brick.guid)
                touchedBrick.healthPoint -= self.Ball.damage
                print(self.Ball.damage)
                if touchedBrick.healthPoint <= 0:
                    brick.kill()
            return True
        return False

    def loseLife(self):
        # perd vie
        self.vie -= 1
        # remet la taille de base
        self.Ball.sprite.width = 25.6
        self.Ball.sprite.height = 25.6
        # replace la balle au centre
        self.Ball.sprite.center_x = SCREEN_WIDTH / 2
        self.Ball.sprite.center_y = SCREEN_HEIGHT / 2 - 50
        # vitesse à zéro
        self.Ball.sprite.change_x = 0
        self.Ball.sprite.change_y = 0
        # met en pause le jeu
        self.wait = True

    def endGame(self):
        game_over_view = GameOverView(self.time_taken, self.score)
        self.window.show_view(game_over_view)
        self.background_music.stop(self.media_player)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        self.platform.sprite.center_x = x

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        # Récupère le sprite cliqués
        # cards = arcade.get_sprites_at_point((x, y), *sprite list des blocks*)
        if self.wait:
            self.Ball.sprite.change_x = 0
            self.Ball.sprite.change_y = - BALL_SPEED
            self.wait = False
        else:
            bricksClicked = arcade.get_sprites_at_point((_x, _y), self.scene["Bricks"])
            if len(bricksClicked) > 0:
                for brick in bricksClicked:
                    print(brick)
                    brick.kill()

    def on_mouse_scroll(self, x: int, y: int, scroll_x: int, scroll_y: int):
        multiplicator = 0
        if scroll_y > 0: multiplicator = 3
        if scroll_y < 0: multiplicator = 4
        self.Ball.sprite.width += scroll_y * multiplicator
        self.Ball.sprite.height += scroll_y * multiplicator

        if 150 < self.Ball.sprite.width:
            self.Ball.sprite.width = 150
            self.Ball.sprite.height = 150
        if 3 > self.Ball.sprite.width:
            self.Ball.sprite.width = 3
            self.Ball.sprite.height = 3

        self.Ball.modify_damage()


class GameWinView(arcade.View):
    def __init__(self, timer, score, level):
        super().__init__()
        self.timer_text = arcade.Text(
            text="00:00:00",
            start_x=SCREEN_WIDTH // 2,
            start_y=SCREEN_HEIGHT // 2 - 50,
            color=arcade.color.WHITE,
            font_size=100,
            anchor_x="center",
        )
        self.timer = timer
        self.score = score
        self.beatenLevel = level

    def on_show_view(self):
        arcade.set_background_color(arcade.color.BLACK_OLIVE)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("YOU WON !", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, arcade.color.WHITE, 54, anchor_x="center")
        arcade.draw_text("Click to restart", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 75, arcade.color.WHITE, 24,
                         anchor_x="center")

        # timer
        # Calculate minutes
        minutes = int(self.timer) // 60
        # Calculate seconds by using a modulus (remainder)
        seconds = int(self.timer) % 60
        # Calculate 100s of a second
        seconds_100s = int((self.timer - seconds) * 100)
        # Use string formatting to create a new text string for our timer
        self.timer_text.text = f"{minutes:02d}:{seconds:02d}:{seconds_100s:02d}"

        # time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {self.timer_text.text}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT / 2 - 150,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        arcade.draw_text(f"Score : {self.score}",
                         SCREEN_WIDTH / 2,
                         SCREEN_HEIGHT - 100,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        # output_total = f"Total Score: {self.window.total_score}"
        # arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if self.beatenLevel.isAnyLevelLeft():
            level = Level(self.beatenLevel.levelNumber + 1, "./Assets/fond_jeu.jpg")
        else:
            level = Level(1, "./Assets/fond_jeu.jpg")

        game_view = GameView(level)
        self.window.show_view(game_view)

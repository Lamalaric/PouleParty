import arcade
from constant import *


class Brick(arcade.Sprite):
    """Classe decrivant le fonctionnement d'une brick."""

    """Constructeur de classe"""

    def __init__(self, healthPoint, position, size, sprite, id, path):
        super().__init__()
        self.id = id
        self.healthPoint = healthPoint
        self.position = position
        self.size = size
        self.sprite = sprite
        self.image_path = path
        self.sprite.position = position

    @staticmethod
    def fromJson(data, y):
        bricksLine = []
        health = data["health"]
        size = data["scale"]

        brick_spacing = SCREEN_WIDTH / (data["bricksNumber"] + 1)

        for i in range(data["bricksNumber"]):
            if 3 <= health < 1000:
                path = f"./assets/brique_metal.png"
            elif health >= 1000:
                path = f"./assets/brique_noire.png"
            else:
                path = f"./assets/brique.png"

            sprite = arcade.Sprite(path, size)
            x = (i + 1) * brick_spacing

            sprite.position = (x, y)

            # Concat x and y as a string to create a unique id
            brick = Brick(health, sprite.position, size, sprite, str(x) + "-" + str(y), path)

            bricksLine.append(brick)

        return bricksLine

    """Détruire la brick lorsqu'elle n'a plus de vie"""

    def die(self):
        pass

    def setDefaultTexture(self):
        self.sprite.append_texture(arcade.load_texture(self.imagePath))
        self.sprite.set_texture(1)

        return
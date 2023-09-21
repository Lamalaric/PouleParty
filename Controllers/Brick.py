import arcade
from constant import *

class Brick(arcade.Sprite):
    """Classe decrivant le fonctionnement d'une brick."""

    """Constructeur de classe"""

    def __init__(self, healthPoint, position, size, sprite):
        super().__init__()
        self.healthPoint = healthPoint
        self.position = position
        self.size = size
        self.sprite = sprite
        self.sprite.position = position

    """Retirer des points de vie à la brick"""

    def updateHealthPoint(self, healthPointToRemove):
        if self.healthPoint - healthPointToRemove <= 0:
            self.die()
            return

        self.healthPoint -= healthPointToRemove

        return self.healthPoint

    @staticmethod
    def fromJson(data, y):
        bricksLine = []

        for i in range(data["bricksNumber"]):
            health = data["health"]
            size = data["scale"]
            sprite = arcade.Sprite(f"./assets/brique.png", size)
            x = SCREEN_WIDTH / 2 // data["bricksNumber"]

            x += sprite.width - (SCREEN_WIDTH / 2 * i)
            sprite.position = (x, y)

            brick = Brick(health, sprite.position, size, sprite)

            bricksLine.append(brick)

        return bricksLine

    """Détruire la brick lorsqu'elle n'a plus de vie"""

    def die(self):
        pass

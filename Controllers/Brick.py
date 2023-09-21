import arcade
from constant import *

class Brick(arcade.Sprite):
    """Classe decrivant le fonctionnement d'une brick."""

    """Constructeur de classe"""
    def __init__(self, healthPoint, position, size):
        super().__init__()
        self.healthPoint = healthPoint
        self.position = position
        self.size = size
        self.sprite = sprite
        self.sprite.position = position

    """Retirer des points de vie à la brick"""
    def __updateHealthPoint(self, healthPointToRemove):
        if self.__healthPoint - healthPointToRemove <= 0:
            self.die()
            return

        self.__healthPoint -= healthPointToRemove

        return self.__healthPoint

    @staticmethod
    def fromJson(data, y):
        bricksLine = []

        for i in range(data["bricksNumber"]):
            health = data["health"]
            size = data["scale"]
            sprite = arcade.Sprite(f"./assets/brique.png", size)

            x = SCREEN_WIDTH / data["bricksNumber"]
            x += sprite.width * i + 1
            position = (x, y)

            brick = Brick(health, position, size, sprite)


            bricksLine.append(brick)
            x += 50

        return bricksLine

    """Détruire la brick lorsqu'elle n'a plus de vie"""

    def die(self):
        pass



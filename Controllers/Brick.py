import arcade


class Brick(arcade.Sprite):
    """Classe decrivant le fonctionnement d'une brick."""

    """Constructeur de classe"""
    def __init__(self, healthPoint, position, size, type):
        super().__init__()
        self.__healthPoint = healthPoint
        self.__position = position
        self.__size = size
        self.__type = type
        self.__imagePath = f"./assets/{type}.png"
        self.__sprite = arcade.Sprite(self.__imagePath, self.__size)

    """Retirer des points de vie à la brick"""
    def __updateHealthPoint(self, healthPointToRemove):
        if (self.healthPoint - healthPointToRemove <= 0):
            self.die()
            return

        self.healthPoint -= healthPointToRemove

        return self.healthPoint

    @staticmethod
    def fromJson(data):
        hp = data["hp"]
        position = data["position"]
        size = data["size"]
        return Brick(hp, position, size)

    """Détruire la brick lorsqu'elle n'a plus de vie"""
    def __die(self):
        pass



import arcade


class Brick(arcade.Sprite):
    """Classe decrivant le fonctionnement d'une brick."""

    """Constructeur de classe"""
    def __init__(self, healthPoint, position, size):
        super().__init__()
        self.__healthPoint = healthPoint
        self.__position = position
        self.__size = size
        self.__imagePath = f"./assets/brique.png"
        self.sprite = arcade.Sprite(self.__imagePath, size)

    """Retirer des points de vie à la brick"""
    def __updateHealthPoint(self, healthPointToRemove):
        if self.__healthPoint - healthPointToRemove <= 0:
            self.die()
            return

        self.__healthPoint -= healthPointToRemove

        return self.__healthPoint

    @staticmethod
    def fromJson(data):
        hp = data["hp"]
        position = data["position"]
        size = data["size"]

        return Brick(hp, position, size)

    """Détruire la brick lorsqu'elle n'a plus de vie"""
    def __die(self):
        pass



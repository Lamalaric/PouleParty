

class Brick:
    """Classe decrivant le fonctionnement d'une brick."""

    """Constructeur de classe"""
    def __init__(self, healthPoint, position, size):
        self.healthPoint = healthPoint
        self.position = position
        self.size = size

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



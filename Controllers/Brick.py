class Brick:
    """Classe decrivant le fonctionnement d'une brick."""

    def __init__(self, healthPoint, position, size):
        """Constructeur de classe"""
        self.healthPoint = healthPoint
        self.position = position
        self.size = size

    def __updateHealthPoint(self, healthPointToRemove):
        """Retirer des points de vie à la brick"""
        if self.healthPoint - healthPointToRemove <= 0:
            self.die()

            return

        self.healthPoint -= healthPointToRemove

        return self.healthPoint

    def __die(self):
        """Détruire la brick lorsqu'elle n'a plus de vie"""




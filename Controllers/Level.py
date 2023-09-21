import os
import json

from Controllers.Brick import Brick
from constant import *


class Level:
    def __init__(self, levelNumber, imagePath):
        self.brickLines = []
        self.background = imagePath
        self.levelNumber = levelNumber
        self.instantiate()

    def isLevelCompleted(self):
        return len(self.brickLines) == 0

    def actualizeBricks(self):
        # Regarder si y'a pas des maps ou similaire pour réduire la complexité O(n)
        bricks_to_remove = []
        for brick in self.brickLines:
            if brick.healthPoint <= 0:
                bricks_to_remove.append(brick)

        for brick in bricks_to_remove:
            self.brickLines.remove(brick)

    def isAnyLevelLeft(self):
        json_filename = f"levels.json"
        json_path = os.path.join("./levels/", json_filename)

        if os.path.exists(json_path):
            with open(json_path, 'r') as json_file:
                data = json.load(json_file)
                level_data = data.get(f"level{self.levelNumber + 1}")

                if level_data:
                    return True

        return False

    def getBrickById(self, brickId):
        for brickLine in self.brickLines:
            for brick in brickLine:
                if brick.id == brickId:
                    return brick

    # Fill the Brick list with the bricks from the JSON file
    # The JSON file is named "levelX.json", where X is the level number.
    def instantiate(self):
        json_filename = f"levels.json"
        json_path = os.path.join("./levels/", json_filename)

        if os.path.exists(json_path):
            with open(json_path, 'r') as json_file:
                data = json.load(json_file)
                level_data = data.get(f"level{self.levelNumber}")

                if level_data:
                    y = SCREEN_HEIGHT - 150
                    for brick_data in level_data:
                        self.brickLines.append(Brick.fromJson(brick_data, y))
                        y -= 65

        else:
            print(f"JSON file '{json_filename}' not found for level {self.levelNumber}.")

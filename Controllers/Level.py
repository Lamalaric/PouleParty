import os
import json

from Controllers.Brick import Brick


class Level:
    def __init__(self, levelNumber, imagePath):
        self.level_number = None
        self.bricks = []
        self.background = imagePath
        self.levelNumber = levelNumber
        self.instantiate()

    def isLevelCompleted(self):
        return len(self.bricks) == 0

    def actualizeBricks(self):
        # Regarder si y'a pas des maps ou similaire pour réduire la complexité O(n)
        bricks_to_remove = []
        for brick in self.bricks:
            if brick.healthPoint <= 0:
                bricks_to_remove.append(brick)

        for brick in bricks_to_remove:
            self.bricks.remove(brick)

    # Fill the Brick list with the bricks from the JSON file
    # The JSON file is named "levelX.json", where X is the level number.
    def instantiate(self):
        json_filename = f"level{self.levelNumber}.json"
        json_path = os.path.join("./levels/", json_filename)

        if os.path.exists(json_path):
            with open(json_path, 'r') as json_file:
                data = json.load(json_file)

                for brick_data in data:
                    brick = Brick.fromJson(brick_data)
                    self.bricks.append(brick)
        else:
            print(f"JSON file '{json_filename}' not found for level {self.level_number}.")

from config import *
import json, os

# Score class
class Score:
    # Init score class
    def __init__(self):
        # Create a json file with score and data if not exists
        if not os.path.isfile(DATA_FILE):
            with open(DATA_FILE, mode="w") as file:
                json.dump(DATA_TEMPLATE,file)

    # Save score after winning or losing the game
    def save(self, win : bool):
        data = self.load()
        data["games"] += 1
        if win: data["wins"] += 1
        else: data["loses"] += 1
        with open(DATA_FILE, mode="w") as file:
                json.dump(data,file)

    # Load data and score
    def load(self):
        with open(DATA_FILE, mode="r") as file:
                data = json.load(file)
        return data
        
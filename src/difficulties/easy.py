from src.base_classes.difficulty import Difficulty


class EasyDifficulty(Difficulty):
    def __init__(self, owner):
        self.difficulty = "Easy"
        self.time_left = 60
        super().__init__(owner)
        
from src.base_classes.difficulty import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        self.difficulty = "Hard"
        super().__init__(owner)
        
from src.base_classes.difficulty import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        HardDifficulty.difficulty = "Easy"
        super().__init__(owner)
        
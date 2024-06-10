from src.base_classes.difficulty import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        super().__init__(owner)
        HardDifficulty.str_difficulty = "Easy"
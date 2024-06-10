from src.base_classes.difficulty import Difficulty


class EasyDifficulty(Difficulty):
    def __init__(self, owner):
        EasyDifficulty.str_difficulty = "Easy"
        super().__init__(owner)
        
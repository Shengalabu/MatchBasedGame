from src.base_classes.difficulty import Difficulty


class EasyDifficulty(Difficulty):
    def __init__(self, owner):
        super().__init__(owner)
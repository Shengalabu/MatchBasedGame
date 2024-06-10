from src.base_classes.dificulty import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        super().__init__(owner)
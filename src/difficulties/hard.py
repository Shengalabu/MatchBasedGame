from base_classes.level import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        super().__init__(owner)
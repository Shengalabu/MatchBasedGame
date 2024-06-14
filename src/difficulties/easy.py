from src.libraries.color_library import Colors
from src.libraries import ascii_library
from src.base_classes.difficulty import Difficulty


class EasyDifficulty(Difficulty):
    def __init__(self, owner):
        # modifiable
        self.difficulty = f"""{Colors.BI_Green}𝐸𝑎𝑠𝑦{Colors.Reset}"""
        # modifiable
        self.time_left = 60
        super().__init__(owner)
        
from src.libraries.color_library import Colors
from src.libraries import ascii_library
from src.base_classes.difficulty import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        # modifiable
        self.difficulty = f"""{Colors.BI_Red}廾闩尺ᗪ{Colors.Reset}""" 
        # modifiable
        self.time_left = 30      
        super().__init__(owner)
        
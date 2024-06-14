from src.libraries.color_library import Colors
from src.libraries import ascii_library
from src.base_classes.difficulty import Difficulty


class HardDifficulty(Difficulty):
    def __init__(self, owner):
        # modifiable
        self.difficulty = f"""{Colors.BI_Red}廾闩尺ᗪ{Colors.Reset}""" 
        # modifiable
        self.time_left = 3      
        # modifiable
        self.question_data = [["0", ascii_library.ascii_list[0], ["Yellow", "A fruit", "Filled with Pottatium"], ["Banana", "Apple", "Yellow Mango"], 0],
                ["1", ascii_library.ascii_list[1], ["Hot individual", "An Ogre", "Has a movie"], ["Puss In Boots", "Denji", "Shrek"], 2]
            ]
        super().__init__(owner)
        
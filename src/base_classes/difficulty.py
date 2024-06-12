from src.libraries import util_library
from src.menus.question_widget_displayer import QuestionDisplay
from src.base_classes.level import Level
import random

class Difficulty(Level):
    difficulty = "No difficulty selected"
    question_display_inst = None
    question_data = [["Color Yellow", "Filled With Pottasium", "A Fruit", "Banana"]
                    ]
    
    
    
    def __init__(self, owner):
        super().__init__(owner)
        self.create_question_displayer()
        self.display_question()
        
    def create_question_displayer(self):
        Difficulty.question_display_inst = QuestionDisplay(self)
        
    def display_question(self):
        util_library.clear_console()
        print(Difficulty.question_display_inst.display_question(Difficulty.difficulty, Difficulty.question_data[random.randrange(len(Difficulty.question_data))]))
        #Difficulty.question_display_inst.display_question(Difficulty.str_difficulty, Difficulty.question_data[random.randrange(len(Difficulty.question_data))])
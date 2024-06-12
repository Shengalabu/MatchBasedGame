from src.libraries import util_library
from src.libraries import ascii_library
from src.menus.question_widget_displayer import QuestionDisplay
from src.base_classes.level import Level


import random


class Difficulty(Level):
    difficulty = "No difficulty selected"
    question_display_inst = None
    
    
    #index, ASCII_Index, HintArray, PossibleAnswerArray, CorrectAnswerIndex
    question_data = [["0", ascii_library.ascii_list[0], ["Yellow", "A fruit", "Filled with Pottatium"], ["Banana", "Apple", "Yellow Mango"], 0],
                     ["1", ascii_library.ascii_list[1], ["Hot individual", "An Ogre", "Has a movie"], ["Puss In Boots", "Denji", "Shrek"], 2]
                    ]
    
    
    
    def __init__(self, owner):
        super().__init__(owner)
        self.create_question_displayer()
        self.display_question()
        
    def create_question_displayer(self):
        Difficulty.question_display_inst = QuestionDisplay(self)
        
    def display_question(self):
        util_library.clear_console()
        Difficulty.question_display_inst.display_question(Difficulty.difficulty, Difficulty.question_data[random.randrange(len(Difficulty.question_data))])
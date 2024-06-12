from src.base_classes.thread_timer import BackgroundTimer
from src.libraries import util_library
from src.libraries import ascii_library
from src.menus.question_widget_displayer import QuestionDisplay
from src.base_classes.level import Level


import random


class Difficulty(Level):
    difficulty = "No difficulty selected"
    question_display_inst = None
    player_points = 0
    finished_questions = []
    timer_inst = None
    
    
    #index, ASCII_Index, HintArray, PossibleAnswerArray, CorrectAnswerIndex
    question_data = [["0", ascii_library.ascii_list[0], ["Yellow", "A fruit", "Filled with Pottatium"], ["Banana", "Apple", "Yellow Mango"], 0],
                     ["1", ascii_library.ascii_list[1], ["Hot individual", "An Ogre", "Has a movie"], ["Puss In Boots", "Denji", "Shrek"], 2]
                    ]
    
    
    
    def __init__(self, owner):
        super().__init__(owner)
        self.create_question_displayer()
        self.start_questioning()
        
    def start_questioning(self):
        self.timer_inst = BackgroundTimer(30, self)
        
    def create_question_displayer(self):
        Difficulty.question_display_inst = QuestionDisplay(self)
        
    def display_question(self):
        util_library.clear_console()
        Difficulty.question_display_inst.display_question(Difficulty.difficulty, Difficulty.question_data[random.randrange(len(Difficulty.question_data))])
        
    def player_got_correct_answer(self, points, question_index):
        Difficulty.player_points += points
        Difficulty.finished_questions.append(question_index) 
        self.display_question()
    
    def player_failed_to_answer(self, question_index):
        Difficulty.finished_questions.append(question_index) 
        self.display_question()
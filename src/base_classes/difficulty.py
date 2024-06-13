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
        self.timer_inst = BackgroundTimer(60, self)
        self.display_new_question("     ")
        
    def run_timer_task(self, time_left):
        self.refresh_question_display(time_left)
        
    def create_question_displayer(self):
        self.question_display_inst = QuestionDisplay(self)
        
    def display_new_question(self, time_left):
        self.clear_console()
        self.question_display_inst.display_new_question(self.difficulty, self.question_data[random.randrange(len(self.question_data))], time_left)
        
    def player_got_correct_answer(self, points, question_index):
        self.player_points += points
        self.finished_questions.append(question_index) 
        self.display_new_question("     ")  
    
    def player_failed_to_answer(self, question_index):
        self.finished_questions.append(question_index) 
        self.display_new_question("     ")
        
    def refresh_question_display(self, time_left):
        self.question_display_inst.refresh_display_question(time_left)
    
    def times_up(self):
        pass
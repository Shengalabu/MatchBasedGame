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
        self.display_new_question("00:00")
        
    def run_timer_task(self, time_left):
        self.refresh_question_display(time_left)
        self.question_display_inst.process_input()  # Process input every time the timer updates
        
    def create_question_displayer(self):
        self.question_display_inst = QuestionDisplay(self)
        
    def display_new_question(self, time_left):
        self.clear_console()
        question = random.choice(Difficulty.question_data)
        self.question_display_inst.display_new_question(Difficulty.difficulty, question, time_left)
        
    def player_got_correct_answer(self, points, question_index):
        self.player_points += points
        self.finished_questions.append(question_index) 
        self.display_new_question("00:00")  
    
    def player_failed_to_answer(self, question_index):
        self.finished_questions.append(question_index) 
        self.display_new_question("00:00")
        
    def refresh_question_display(self, time_left):
        self.question_display_inst.refresh_display_question(time_left)
    
    def times_up(self):
        print("Time's up!")
        self.timer_inst.stop_timer()  # Ensure the timer is stopped
        self.owner.display_main_menu()
    
    def stop(self):
        if self.timer_inst:
            self.timer_inst.stop_timer()  # Stop the timer if it's running
        self.question_display_inst.stop()  # Stop the input handling thread

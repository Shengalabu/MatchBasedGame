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
    time_left = 0
    
    
    #index, ASCII_Index, HintArray, PossibleAnswerArray, CorrectAnswerIndex
    question_data = [["0", ascii_library.ascii_list[0], ["Yellow", "A fruit", "Filled with Pottatium"], ["Banana", "Apple", "Yellow Mango"], 0],
                     ["1", ascii_library.ascii_list[1], ["Hot individual", "An Ogre", "Has a movie"], ["Puss In Boots", "Denji", "Shrek"], 2]
                    ]
    
    def __init__(self, owner):
        super().__init__(owner)
        self.create_question_displayer()
        self.start_questioning()
    
    def get_raw_time_left(self):
        return self.time_left
    
    def get_time_left(self):
        timeleft = self.time_left
        mins, secs = divmod(timeleft, 60)
        time_formated = '{:02d}:{:02d}'.format(mins, secs)
        return time_formated
    
    def get_player_points(self):
        return self.player_points
        
    #Not really used since the changing of initial time is handled in the child class
    def get_initial_time(self):
        return 60 if self.difficulty == "easy" else 30
    
    def start_questioning(self):
        self.timer_inst = BackgroundTimer(self.time_left, self)
        self.display_new_question()
        
    def run_timer_task(self, raw_time_left):
        self.time_left = raw_time_left
        self.refresh_question_display()
        
    def create_question_displayer(self):
        self.question_display_inst = QuestionDisplay(self)
        
    def display_new_question(self):
        self.clear_console()
        self.question_display_inst.display_new_question(self.difficulty, self.question_data[random.randrange(len(self.question_data))])
        
    def player_got_correct_answer(self, points, question_index):
        self.player_points += points
        self.finished_questions.append(question_index) 
        self.display_new_question()  
    
    def player_failed_to_answer(self, question_index):
        self.finished_questions.append(question_index) 
        self.display_new_question()
        
    def refresh_question_display(self):
        self.question_display_inst.refresh_display_question()
        
    def player_wants_to_stop(self):
        self.stop_timer()

    def stop_timer(self):
        self.timer_inst.stop_timer()
    
    def times_up(self):
        self.clear_console()
        print("Thanks for playing. Your score is: " + str(self.player_points))
        self.delay(1)
        self.owner.display_main_menu()    
    
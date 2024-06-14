from src.base_classes.terminal_display import TerminalDisplay
from src.base_classes.actor import Actor
import threading
from concurrent.futures import ThreadPoolExecutor

class QuestionDisplay(TerminalDisplay):
    current_question_data = None
    max_current_tries = 2
    current_tries = 2
    difficulty = None
    
    def __init__(self, owner):
        super().__init__(owner)
        self.executor = ThreadPoolExecutor()
        
    def display_new_question(self, difficulty, question_data):
        self.current_question_data = question_data
        self.difficulty = difficulty
        self.refresh_display_question()
        self.thread_take_user_input()
        
        
    def refresh_display_question(self):
        self.clear_console()
        print(
        f"""
=================================================================                             
                            
    {self.difficulty} | {self.owner.get_time_left()} | {self.owner.get_player_points()}pts | Match the given: 
                {self.current_question_data[1]}
    
                              
                                            
    {self.current_question_data[2][0]} || {self.current_question_data[2][1]} || {self.current_question_data[2][2]}                       
    
    1 - {self.current_question_data[3][0]}
    2 - {self.current_question_data[3][1]}
    3 - {self.current_question_data[3][2]}

        
=================================================================
        """
        )
    
    def take_user_input(self):
        take_input = input("Input: ")
        return take_input
    
    def callback(self, future):
        variable = future.result()
        self.evaluate_player_answer(variable)
    
    def thread_take_user_input(self):
        future = self.executor.submit(self.take_user_input)
        future.result(self.owner.get_raw_time_left())
        future.add_done_callback(self.callback)
    
    def end_all_functions(self):
        self.stop_thread()
        self.owner.player_wants_to_stop()
                
    def evaluate_player_answer(self, user_input):
        if self.owner.get_raw_time_left() <= 0:
            self.end_all_functions()
        if user_input == "x":
            self.end_all_functions()
            return  
        if user_input.isdigit():
            user_input = int(user_input) - 1    
            if user_input == self.current_question_data[4]:
                self.display_correct()
            else:
                self.display_wrong()
        else:
            self.display_wrong()
            
    def display_correct(self):
        self.clear_console()
        print("""
=================================================================  


                
            █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀▀ ▀█▀
            █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▄ ░█░
            
            

=================================================================
                  """)
        self.delay(0.5)
        self.owner.player_got_correct_answer(self.current_tries * 5, self.current_question_data[0])
        
    def display_wrong(self):
        self.current_tries -= 1
        self.clear_console()
        print("""
=================================================================  

     
     

             █░█░█ █▀█ █▀█ █▄░█ █▀▀
             ▀▄▀▄▀ █▀▄ █▄█ █░▀█ █▄█

            

=================================================================
                  """)
        self.delay(0.5)
        if self.current_tries > 0:
            self.display_new_question(self.difficulty, self.current_question_data)
        if self.current_tries <= 0:
            self.current_tries = self.max_current_tries
            self.owner.player_failed_to_answer(self.current_question_data[0])
    
    def stop_thread(self):
        self.executor.shutdown(wait=True)
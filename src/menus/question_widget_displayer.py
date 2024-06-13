from src.base_classes.terminal_display import TerminalDisplay
from src.base_classes.actor import Actor
import threading
import queue
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

class QuestionDisplay(TerminalDisplay):
    current_question_data = None
    max_current_tries = 2
    current_tries = 2
    difficulty = None
    active_thread = None
    input_queue = queue.Queue()
    
    def __init__(self, owner):
        super().__init__(owner)
        self.input_queue = queue.Queue()
        self._stop_event = threading.Event()
        self.thread0 = None  # Initialize thread attribute
        
    def display_new_question(self, difficulty, question_data, time_left):
        self.current_question_data = question_data
        self.difficulty = difficulty
        self.refresh_display_question(time_left)
<<<<<<< Updated upstream
        self._stop_event.clear()
        
        if self.thread0 and self.thread0.is_alive():
            self._stop_event.set()
            self.thread0.join()

        self.thread0 = threading.Thread(target=self.get_user_input)
        self.thread0.start()  # Start a new thread to handle user input
=======
        self.active_thread = threading.Thread(target=self.get_player_input, args=(self.input_queue,))
        self.active_thread.start()
>>>>>>> Stashed changes
        
    def refresh_display_question(self, time_left):
        self.clear_console()
        print(
        f"""
=================================================================                             
                            
    {self.difficulty} | {time_left} | Match the given: 
                {self.current_question_data[1]}
    
                              
                                            
    {self.current_question_data[2][0]} || {self.current_question_data[2][1]} || {self.current_question_data[2][2]}                       
    
    1 - {self.current_question_data[3][0]}
    2 - {self.current_question_data[3][1]}
    3 - {self.current_question_data[3][2]}

        
=================================================================
        """
        )
        
<<<<<<< Updated upstream
    def get_user_input(self):
        while not self._stop_event.is_set():
            take_input = input("Input: ")
            self.input_queue.put(take_input)
            if take_input == "x":
                self._stop_event.set()
                self.owner.owner.display_main_menu()
                return
    
    def process_input(self):
        while not self.input_queue.empty():
            take_input = self.input_queue.get()
            
            if take_input == "x":
                self.owner.owner.display_main_menu()
                return
            
            try: 
                take_input = int(take_input)
            except ValueError:
                self.clear_console()
                print("Invalid input. Please try again.")
                self.delay(0.24)
                self.refresh_display_question("00:00")
                continue
            
            if take_input == self.current_question_data[4]:
                self.display_correct(self.current_question_data)
                return
            else:
                self.display_wrong(self.difficulty, self.current_question_data)
                return
=======
    
    def get_player_input(self):
        while True:
            user_input = input("Input: ")
            self.input_queue.put(user_input)
            self.delay(0.1)
    
    def tick_player_answer(self, take_input):
        while True:
            if not self.input_queue.empty():
                self.user_input = self.input_queue.get()
                self.evaluate_player_answer(self.user_input)
            self.delay(0.1)
        
        self.active_thread.join()
            
    def evaluate_player_answer(self, take_input):
        if take_input == "x":
            self.owner.owner.display_main_menu()
        try: 
            take_input = int(take_input)
        except:
            self.clear_console()
            print("Invalid input. Please try again.")
            self.delay(0.24)
            self.refresh_display_question("     ")
        if take_input == self.current_question_data[4]:
            self.display_correct()
        else:
            self.display_wrong()
>>>>>>> Stashed changes
            
    def display_correct(self):
        self.clear_console()
        print("""
=================================================================  


                
            █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀▀ ▀█▀
            █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▄ ░█░
            
            

=================================================================
                  """)
        self.delay(0.5)
<<<<<<< Updated upstream
        self.owner.player_got_correct_answer(self.current_tries * 5, question_data[0])
=======
        self.owner.player_got_correct_answer(self.current_tries*5, self.current_question_data[0])
>>>>>>> Stashed changes
        
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
<<<<<<< Updated upstream
            self.display_new_question(difficulty, question_data, "00:00")
        if self.current_tries <= 0:
            self.current_tries = self.max_current_tries
            self.owner.player_failed_to_answer(question_data[0])
    
    def stop(self):
        self._stop_event.set()
        if self.thread0 and self.thread0.is_alive():
            self.thread0.join()
=======
            self.display_new_question(self.difficulty, self.current_question_data, "     ")
        if self.current_tries <= 0:
            self.current_tries = self.max_current_tries
            self.owner.player_failed_to_answer(self.current_question_data[0])
        
>>>>>>> Stashed changes

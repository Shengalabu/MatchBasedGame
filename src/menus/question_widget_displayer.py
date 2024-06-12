from src.base_classes.terminal_display import TerminalDisplay
from src.base_classes.actor import Actor


class QuestionDisplay(TerminalDisplay):
    current_question_data = None
    max_current_tries = 2
    current_tries = 2
    difficulty = None
    
    def __init__(self, owner):
        super().__init__(owner)
        
    def display_new_question(self, difficulty, question_data, time_left):
        self.current_question_data = question_data
        self.difficulty = difficulty
        self.refresh_display_question(time_left)
        
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
        input("Input: ")
        self.evaluate_player_answer()
    
    def evaluate_player_answer(self):
        take_input = input("Input: ")
        
        if take_input == "x":
            self.owner.owner.display_main_menu()
        
        try: 
            take_input = int(take_input)
        except:
            self.clear_console()
            print("Invalid input. Please try again.")
            self.delay(0.24)
            self.refresh_display_question("     ")
            
        if take_input == self.question_data[4]:
            self.display_correct(self.question_data)
        else:
            self.display_wrong(self.difficulty, self.question_data)
            
    def display_correct(self, question_data):
        self.clear_console()
        print("""
=================================================================  


                
            █▀▀ █▀█ █▀█ █▀█ █▀▀ █▀▀ ▀█▀
            █▄▄ █▄█ █▀▄ █▀▄ ██▄ █▄▄ ░█░
            
            

=================================================================
                  """)
        self.delay(0.5)
        self.owner.player_got_correct_answer(self.current_tries*5, question_data[0])
        
    def display_wrong(self, difficulty, question_data):
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
            self.display_new_question(difficulty, question_data, "     ")
        if self.current_tries <= 0:
            self.current_tries = self.max_current_tries
            self.owner.player_failed_to_answer(question_data[0])
        
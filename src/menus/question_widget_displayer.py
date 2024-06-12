from src.base_classes.terminal_display import TerminalDisplay
from src.base_classes.actor import Actor


class QuestionDisplay(TerminalDisplay):
    current_question_data = None
    max_current_tries = 2
    current_tries = 2
    
    def __init__(self, owner):
        super().__init__(owner)
        
    def display_question(self, difficulty, question_data):
        self.clear_console()
        self.current_question_data = question_data
        print(
        f"""
=================================================================                             
                            
    {difficulty} | Match the given:
                {question_data[1]}
    
                              
                                            
    {question_data[2][0]} || {question_data[2][1]} || {question_data[2][2]}                       
    
    1 - {question_data[3][0]}
    2 - {question_data[3][1]}
    3 - {question_data[3][2]}

        
=================================================================
        """
        )
        self.evaluate_player_answer(difficulty, question_data)
        
        
    def evaluate_player_answer(self, difficulty, question_data):
        take_input = input("Input: ")
        
        if not take_input.isdigit():
            if take_input == "x":
                self.owner.owner.display_main_menu()
        
        take_input = int(take_input)-1
        
        if take_input == question_data[4]:
            self.display_correct(question_data)
        else:
            self.display_wrong(difficulty, question_data)
            
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
            self.display_question(difficulty, question_data)
        if self.current_tries <= 0:
            self.current_tries = self.max_current_tries
            self.owner.player_failed_to_answer(question_data[0])
        
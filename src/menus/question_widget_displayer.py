from src.base_classes.terminal_display import TerminalDisplay
from src.base_classes.actor import Actor


class QuestionDisplay(TerminalDisplay):
    def __init__(self, owner):
        super().__init__(owner)
        
    def display_question(self, difficulty, question_data):
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
        take_input = int(input("Input: "))-1
        if take_input == question_data[4]:
            print("Correct!")
        else:
            print("Wrong!") 
        
            
        
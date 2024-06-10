from src.base_classes.terminal_display import TerminalDisplay
from src.base_classes.actor import Actor


class QuestionDisplay(TerminalDisplay):
    def __init__(self, owner):
        super().__init__(owner)
        
    def display_question(self, difficulty, question_data):
        print(
        """
=================================================================                             
     {difficulty}                        
    MATCH THE GIVEN:
    
    
                              
                                            
                        
                        

    
    
    

        
=================================================================
        """
        )
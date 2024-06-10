from src.base_classes.level import Level

class Difficulty(Level):
    str_difficulty = "difficulty"
    
    def __init__(self, owner):
        super().__init__(owner)
        self.display_question()
        
    def display_question(self):
        print(
        """
=================================================================                             
    {str_difficulty}                        
    MATCH THE GIVEN:
                              
                                            
                        
                        

    
    
    

        
=================================================================
        """
        )
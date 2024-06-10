from libraries import util_library
from base_classes.actor import Actor
import src.app as app

class MainMenu(Actor):
    def __init__(self, owner):
        super().__init__(owner)
        
    def invalid_input(self):
        print("Invalid input. Please try again.")
        util_library.delay(1)
        util_library.clear_console()
        
    
    def display_main_menu(self):
        util_library.clear_console()
        print(
        """
        =================================================================
                                                
                                                    
                                MATCHING GAME           
                                                    
                                    Play                
                                    Quit       
        
            Instructions:
                - Match the question.
                - Try not to lose.
                - Win the game.
                
        =================================================================
        """
        )
        take_input = input("Input: ").lower()
        if take_input == "quit":
            if isinstance(self.owner, app.App):
                self.owner.close_app()
        if take_input == "play":
            self.display_difficulty_menu()
        else: 
            self.invalid_input()
            self.display_main_menu()
            

    def display_difficulty_menu(self):
        util_library.clear_console()
        print(
        """
        =================================================================
                                                
                                                    
                              
                              
                              Select Difficulty           
                                                    
                                    Easy                
                                    Hard       
        
         
           
 
        =================================================================
        """
        )
        take_input = input("Input: ").lower()
        if take_input == "easy":
                pass
        if take_input == "hard":
                pass
        else:
            self.invalid_input()
            self.display_difficulty_menu()

    
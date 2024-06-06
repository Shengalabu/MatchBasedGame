from base_classes import util_library
from base_classes.actor import Actor
import app


class MainMenu(Actor):
    def __init__(self, owner):
        super().__init__(owner)
    
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
        if (take_input == "quit"):
            if isinstance(self.owner, app.App):
                self.owner.close_app()
        elif take_input == "play":
            util_library.print_hello_world()
        else:
            print("Invalid input. Please try again.")
            util_library.delay(1)
            util_library.clear_console()
            self.display_main_menu()
        
        

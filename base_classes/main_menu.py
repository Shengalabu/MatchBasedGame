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
        if (input("Input: ").lower() == "quit"):
            if isinstance(self.owner, app.App):
                self.owner.close_app()
        util_library.print_hello_world()
        

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
                - Match the shit.
                - Try not to shit.
                - Win the shit.
                
        =================================================================
        """
        )
        if (input("Input: ").lower() == "quit"):
            self.owner(App)
            # Cast to App here then call close app
        util_library.print_hello_world()
        

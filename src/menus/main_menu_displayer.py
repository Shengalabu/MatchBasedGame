from src.base_classes.terminal_display import TerminalDisplay
from src.libraries import util_library

class MainMenu(TerminalDisplay):
    def __init__(self, owner):
        super().__init__(owner)
        
    def invalid_input(self):
        print("Invalid input. Please try again.")
        util_library.delay(1)
        util_library.clear_console()
        
    def display_main_menu(self):
        from src.app import App  # Local import to avoid circular import
        util_library.clear_console()
        print(
        """
=================================================================
                                        
                                            
                        MATCHING GAME           
                                            
                         1  -  Play                
                         2  -  Quit       

    Instructions:
        - Match the question.
        - Try not to lose.
        - Win the game.
        
=================================================================
        """
        )
        take_input = input("Input: ").lower()
        if take_input == "2":
            if isinstance(self.owner, App):
                self.owner.close_app()
        elif take_input == "1":
            self.display_difficulty_menu()
        else: 
            self.invalid_input()
            self.display_main_menu()

    def display_difficulty_menu(self):
        util_library.clear_console()
        print(
        """
=================================================================
                                        
                                            
                      SELECT DIFFICULTY           
                                            
                         1  -  Easy                
                         2  -  Hard       

    
    
    
    
        
=================================================================
        """
        )
        take_input = input("Input: ").lower()
        if take_input == "1":
            self.owner.create_game_map("easy")
        elif take_input == "2":
            self.owner.create_game_map("hard")
        else:
            self.invalid_input()
            self.display_difficulty_menu()

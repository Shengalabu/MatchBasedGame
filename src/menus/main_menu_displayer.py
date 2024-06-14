from src.libraries.color_library import Colors
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
        f"""
{Colors.Bold}================================================================={Colors.Reset}
                                        
                                            
                      {Colors.Bold}{Colors.Yellow}MⷨAͣᴛⷮCͨн ВAͣS͛EͤDͩ GAͣMⷨEͤ{Colors.Reset}           
                                            
                         1  -  Play                
                         2  -  Quit       

    Instructions:
        - Type in the number to select.
        - Get as much points as you can before the timer runs out.
        - Type X anytime to close the app.
        
{Colors.Bold}================================================================={Colors.Reset}
        """
        )
        take_input = input("Input: ").lower()
        if (take_input == "2") or (take_input == "x"):
            if isinstance(self.owner, App):
                self.owner.close_app()
        elif take_input == "1":
            self.display_difficulty_menu()
        else: 
            self.invalid_input()
            self.display_main_menu()

    def display_difficulty_menu(self):
        self.clear_console()
        print(
        f"""
{Colors.Bold}================================================================={Colors.Reset}
                                        
                                            
                      {Colors.Bold}𝗦𝗘𝗟𝗘𝗖𝗧 𝗗𝗜𝗙𝗙𝗜𝗖𝗨𝗟𝗧𝗬{Colors.Reset}           
                                            
                         {Colors.Bold}{Colors.BI_Green}1  -  𝐸𝑎𝑠𝑦{Colors.Reset}    
                                     
                         {Colors.Bold}{Colors.BI_Red}2  -  H̴̪̦̞̽̓̓a̴͔̝̒͆̓r̵̝͍̠̔͌d̴̢̫̠̀͛{Colors.Reset}       
    
    
    
    
        
{Colors.Bold}================================================================={Colors.Reset}
        """
        )
        take_input = input("Input: ").lower()
        if take_input == "1":
            self.owner.create_game_map("easy")
        elif take_input == "2":
            self.owner.create_game_map("hard")
        elif take_input == "x":
            self.owner.close_app()
        else:
            self.invalid_input()
            self.display_difficulty_menu()

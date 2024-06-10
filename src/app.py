from src.difficulties.easy import EasyDifficulty
from src.difficulties.hard import HardDifficulty
from src.menus.main_menu_displayer import MainMenu
from src.libraries import util_library
from src.base_classes.actor import Actor

class App(Actor):
    main_menu_inst = None  # Class variable
    game_level = None      # Class variable

    def __init__(self, owner=None):
        super().__init__(owner or self)
        self.create_main_menu()
        self.display_main_menu()
    
    def create_main_menu(self):
        App.main_menu_inst = MainMenu(self)
    
    def display_main_menu(self):
        if App.main_menu_inst:
            App.main_menu_inst.display_main_menu()
        else:
            print("Main menu is not created.")
            
    def create_game_map(self, difficulty):
        if difficulty == "easy":
            game_level = EasyDifficulty(self)
        if difficulty == "hard":
            game_level = HardDifficulty(self)
    
    def close_app(self):
        util_library.clear_console()
        print("Cleaning.")
        util_library.delay()
        util_library.clear_console()
        print("Cleaning..")
        util_library.delay()
        util_library.clear_console()
        print("Cleaning...")
        util_library.delay()
        util_library.clear_console()
        exit()



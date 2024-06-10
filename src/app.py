from src.menus.main_menu import MainMenu
from src.libraries import util_library
from src.base_classes.actor import Actor

class App(Actor):
    main_menu_inst = None  # Class variable
    game_map = None

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
            
    def
    
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



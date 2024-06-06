from base_classes.actor import Actor
from base_classes import main_menu
from base_classes import util_library



class App(Actor):
    
    main_menu_inst = None
    
    def __init__(self, owner):
        super().__init__(owner)
        self.create_main_menu()
        self.display_main_menu()
    
    def create_main_menu(self):
        App.main_menu_inst = main_menu.MainMenu(self)
    
    def display_main_menu(self):
        App.main_menu_inst.display_main_menu()
    
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
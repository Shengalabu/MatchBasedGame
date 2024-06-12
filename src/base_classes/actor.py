from src.libraries import util_library

class Actor:
    def __init__(self, owner):
        self.owner = owner
        self.begin_play()
        
    def begin_play(self):
        pass
    
    def clear_console_delayed(self, seconds=0.2):
        self.clear_console()
        self.delay(seconds)
        
    def clear_console(self):
        util_library.clear_console()
        
    def delay(self, seconds):
        util_library.delay(seconds)

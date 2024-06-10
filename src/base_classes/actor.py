from base_classes import util_library

class Actor:
    def __init__(self, owner):
        self.owner = owner
        self.begin_play()
        
    def begin_play(self):
        pass
    
    def clear_console_delayed(self, seconds=0.2):
        util_library.clear_console()
        util_library.delay(seconds)

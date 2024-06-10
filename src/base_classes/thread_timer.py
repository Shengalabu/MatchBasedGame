import threading
import time

from base_classes.actor import Actor

class BackgroundTimer(Actor):
    def __init__(self, seconds, owner):
        super().__init__(owner)
        self.seconds = seconds
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True 
    
    def run(self):
        while self.seconds:
            mins, secs = divmod(self.seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            self.seconds -= 1
        print("Time's up!")
    
    def start(self):
        self.thread.start()

# Example usage:
timer = BackgroundTimer(10)  # Timer for 10 seconds
timer.start()




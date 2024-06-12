import threading
import time

from src.base_classes.actor import Actor

class BackgroundTimer(Actor):
    def __init__(self, seconds, owner):
        super().__init__(owner)
        self.seconds = seconds
        self.thread = threading.Thread(target=self.run)
        self.thread.daemon = True 
        self.start_timer()
    
    def run(self):
        while self.seconds:
            mins, secs = divmod(self.seconds, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            #print(timer, end="\r")
            time.sleep(1)
            self.seconds -= 1
            self.message_owner_tick(str(timer))
        self.message_owner_times_up()
    
    def message_owner_tick(self, time_left):
        self.owner.run_timer_task(time_left)
        
    def message_owner_times_up(self):
        self.owner.times_up()    
        
    def start_timer(self):
        self.thread.start()







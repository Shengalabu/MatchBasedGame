import threading
import time

from src.base_classes.actor import Actor

class BackgroundTimer(Actor):
    def __init__(self, seconds, owner):
        super().__init__(owner)
        self.seconds = seconds
        self.thread = threading.Thread(target=self.run)
        self.stop_event = threading.Event()
        self.thread.daemon = True 
        self.start_timer()
    
    def run(self):
        while self.seconds > 0:
            time.sleep(1)
            self.seconds -= 1
            self.message_owner_tick(self.seconds)
        self.message_owner_times_up()
    
    def message_owner_tick(self, raw_time_left):
        self.owner.run_timer_task(raw_time_left)
        
    def message_owner_times_up(self):
        self.owner.times_up()    
        
    def start_timer(self):
        self.thread.start()
        
    def stop_timer(self):
        self.seconds = 0
        self.stop_event.set()
        self.thread.join()







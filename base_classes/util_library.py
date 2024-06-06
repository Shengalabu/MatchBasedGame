import time
import os

def delay(seconds = 0.2):
    time.sleep(seconds)
    
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_hello_world():
    print("Hello World")
    


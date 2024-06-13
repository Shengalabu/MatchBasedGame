import threading
import time
from concurrent.futures import ThreadPoolExecutor

# Method that runs in a worker thread and produces a variable
def produce_variable():
    time.sleep(2)  # Simulate some processing time
    produced_variable = "Hello from the worker thread!"
    return produced_variable

# Method that processes the variable in the main thread
def process_variable(variable):
    print(f"Main thread received: {variable}")
    # Simulate processing the variable
    time.sleep(1)
    print(f"Main thread processed: {variable}")

# Callback method to be called in the main thread after worker thread completes
def callback(future):
    variable = future.result()
    process_variable(variable)

def main():
    with ThreadPoolExecutor() as executor:
        # Start the worker thread and set the callback
        future = executor.submit(produce_variable)
        future.add_done_callback(callback)

        # Continue doing other tasks in the main thread if needed
        print("Main thread is free to do other tasks...")

        # Wait for the worker thread to complete if necessary
        future.result()  # This will block until the worker thread completes

if __name__ == "__main__":
    main()

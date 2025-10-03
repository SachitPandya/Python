import threading 
from time import sleep

# function to be executed in a new thread
def run():
   # get the current thread
   thread = threading.current_thread()
   # is it a daemon thread?
   print(f'Daemon thread: {thread.daemon}')

# Create a new thread  
thread = threading.Thread(target=run)

# Using the daemon property set the thread as daemon before starting the thread
thread.daemon = True

# start the thread
thread.start()

# Block for a short time to allow the daemon thread to run
sleep(5)

print('Is Main Thread is Daemon thread:', threading.current_thread().daemon)


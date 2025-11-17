import os
import sys
import time
import traceback

def main():
    print(" Script started")
    for i in range(1, 6):
        print(f"Working... step {i}")
        time.sleep(2)
    # Simulate an error (for demo)
    raise Exception(" crash!")

while True:
    try:
        main()
    except Exception as e:
        print("Script crashed!")
        print("Error details:")
        traceback.print_exc()
        print("Restarting \n")
        time.sleep(3)
        # Restart the same script with same arguments
        os.execv(sys.executable, [sys.executable] + sys.argv)

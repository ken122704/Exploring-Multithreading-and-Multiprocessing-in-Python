import multiprocessing
import time
import os

# --- Global Variables for Threading (Shared Memory) ---
# We use a list to store grades as they are processed by threads
curr_grades = []
curr_lock = threading.Lock() # Simple lock to make sure calculations don't crash

def get_user_input():
    print("\n--- Student Grade Computing System ---")
    user_in = input("Enter grades separated by commas (e.g., 90, 85, 92): ")
    try:
        # Turn string input into a list of numbers
        return [int(x.strip()) for x in user_in.split(',')]
    except ValueError:
        print("Invalid input! Using defaults: [85, 90, 78, 92]")
        return [85, 90, 78, 92]
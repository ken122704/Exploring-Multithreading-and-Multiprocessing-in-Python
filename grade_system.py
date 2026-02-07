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

# --- 1. Multithreading Task (Creative: Running Average) ---
def compute_thread(grade, i):
    global curr_grades
    
    # Simulate I/O delay (reading database, etc.)
    time.sleep(0.1)
    
    # Critical Section: Only one thread updates the shared list at a time
    with curr_lock:
        curr_grades.append(grade)
        # Calculate GWA of all grades processed SO FAR
        current_gwa = sum(curr_grades) / len(curr_grades)
        
        print(f" [Thread-{i}] Processed Grade: {grade} | Running GWA: {current_gwa:.2f}")
        
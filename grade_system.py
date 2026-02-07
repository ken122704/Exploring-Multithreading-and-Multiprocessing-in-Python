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
        
def run_threading_logic(grades):
    print("\n>>> Starting Multithreading (Shared Memory)...")
    start = time.time()
    
    # Reset the global list for a fresh run
    global curr_grades
    curr_grades = []
    
    threads = []
    for i, g in enumerate(grades):
        t = threading.Thread(target=compute_thread, args=(g, i+1))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    return time.time() - start

    # --- 2. Multiprocessing Task (Standard: Independent) ---
def compute_process(grade, i):
    # Simulate CPU work
    time.sleep(0.1)
    
    # Processes are independent, so they just calculate their own part
    # They don't know about other processes' grades
    local_avg = grade 
    print(f" [Process-{os.getpid()}] Processed Grade: {grade} | Independent GWA: {local_avg:.2f}")

def run_multiprocessing_logic(grades):
    print("\n>>> Starting Multiprocessing (Independent Memory)...")
    start = time.time()
    
    processes = []
    for i, g in enumerate(grades):
        p = multiprocessing.Process(target=compute_process, args=(g, i+1))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    return time.time() - start
    # --- Main Execution ---
if _name_ == "_main_":
    # 1. Input
    grades_list = get_user_input()
    
    # 2. Run Threads
    t_time = run_threading_logic(grades_list)
    
    # 3. Run Processes
    p_time = run_multiprocessing_logic(grades_list)
    
    # 4. Final Comparison Table
    print("\n" + "="*45)
    print(f"{'Method':<20} | {'Execution Time':<15}")
    print("-" * 45)
    print(f"{'Multithreading':<20} | {t_time:.6f} s")
    print(f"{'Multiprocessing':<20} | {p_time:.6f} s")
    print("="*45)
    
    # Simple observation logic
    if t_time < p_time:
        print("\nObservation: Threads were faster (less overhead).")
    else:
        print("\nObservation: Processes were faster.")
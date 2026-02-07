# Lab: Exploring Multithreading and Multiprocessing in Python

## Q&A

**1. Which approach demonstrates true parallelism in Python? Explain.**
Multiprocessing demonstrates true parallelism. In Python, the `multiprocessing` module creates separate memory spaces and processes for each task. Each process runs on a separate CPU core, allowing them to execute instructions at the exact same time.

**2. Compare execution times between multithreading and multiprocessing.**
* **Multithreading:** Generally faster for this specific lab because the task (calculating a simple average) is very light. The "overhead" (setup time) of creating a thread is small.
* **Multiprocessing:** Likely slower for this specific small task because creating a full new process takes significant system resources (memory, setup time). However, for heavier computations, it would be faster.

**3. Can Python handle true parallelism using threads? Why or why not?**
No, Python cannot handle true parallelism using threads due to the **Global Interpreter Lock (GIL)**. The GIL allows only one thread to execute Python bytecode at a time, even on multi-core processors. Threads essentially "take turns" running so fast that it *looks* parallel, but it is actually concurrent.

**4. What happens if you input a large number of grades (e.g., 1000)? Which method is faster and why?**
If the calculation for each grade is complex (CPU-intensive), **Multiprocessing** would be faster because it utilizes multiple CPU cores simultaneously to crunch the numbers.
* *Note:* If the calculation is trivial (like our simple average), Multithreading might still be faster because the system struggles to manage the "overhead" of creating 1000 separate processes.

**5. Which method is better for CPU-bound tasks and which for I/O-bound tasks?**
* **CPU-bound tasks (Heavy Math/Logic):** Multiprocessing is better (bypasses the GIL).
* **I/O-bound tasks (Waiting for Input/Network/Files):** Multithreading is better (threads can switch while one is waiting).

**6. How did your group apply creative coding or algorithmic solutions in this lab?**
* **Dynamic Input Parsing:** We implemented a robust input handler that accepts comma-separated values, making testing easier than single-entry prompts.
* **Overall GWA Calculation:** We added a main-thread calculation for the "Semester GWA" to provide meaningful context alongside the independent thread processing.
* **Simulated Workload:** We creatively added `time.sleep(0.1)` to simulate a heavier workload, allowing us to actually observe the concurrency differences which would otherwise be too fast to measure.
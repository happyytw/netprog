import threading

# Global variable shared by threads
x = 0

def increment():
    global x
    x += 1

def thread_task(lock):
    for _ in range(300000):
        lock.acquire()  # Acquire lock before accessing the shared data
        increment()
        lock.release()  # Release lock after finishing the access

def main_task():
    global x
    x = 0  # Initialize x as 0
    lock = threading.Lock()  # Create a lock object

    # Create two threads
    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))

    # Start the threads
    t1.start()
    t2.start()

    # Wait for both threads to complete
    t1.join()
    t2.join()

for i in range(10):
    main_task()
    print('Iteration {0}: x = {1}'.format(i, x))

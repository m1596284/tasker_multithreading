import threading
import queue
import time
import random

# Shared queue with a maximum size of 10
queue = queue.Queue(maxsize=10)
lock = threading.Lock()
event = threading.Event()


def producer():
    while not event.is_set():
        num = random.randint(1, 100)
        with lock:
            if not queue.full():
                queue.put(num)
            else:
                continue
        time.sleep(0.1)


def consumer():
    while not event.is_set():
        with lock:
            if not queue.empty():
                num = queue.get()
                print(f"Consumer: Integer is {num}, timer: {time.time() - start_time}")
        time.sleep(0.15)


if __name__ == "__main__":
    # Start the producer and consumer threads
    producer_thread = threading.Thread(target=producer)
    consumer_thread = threading.Thread(target=consumer)
    start_time = time.time()
    producer_thread.start()
    consumer_thread.start()

    # Run the program for 10 seconds
    time.sleep(10)
    event.set()

    # Wait for threads and Stop the program
    producer_thread.join()
    consumer_thread.join()

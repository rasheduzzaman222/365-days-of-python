from queue import Queue
from threading import Thread
import time

def worker(queue):
    while not queue.empty():
        task = queue.get()
        print(f"Processing {task}")
        time.sleep(1)
        queue.task_done()


if __name__ == "__main__":
    task_queue = Queue()

    for i in range(5):
        task_queue.put(f"task-{i}")

    thread = Thread(target=worker, args=(task_queue,))
    thread.start()
    task_queue.join()

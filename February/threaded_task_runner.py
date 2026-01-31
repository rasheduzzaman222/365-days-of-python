from concurrent.futures import ThreadPoolExecutor
import time

def task(n):
    time.sleep(1)
    return f"Task {n} done"

def run_tasks():
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures = [executor.submit(task, i) for i in range(5)]
        for future in futures:
            print(future.result())


if __name__ == "__main__":
    run_tasks()

import os
import time

LOCK_FILE = "process.lock"

def acquire_lock():
    if os.path.exists(LOCK_FILE):
        raise RuntimeError("Another process is running")
    open(LOCK_FILE, "w").close()

def release_lock():
    if os.path.exists(LOCK_FILE):
        os.remove(LOCK_FILE)


if __name__ == "__main__":
    try:
        acquire_lock()
        print("Lock acquired, processing...")
        time.sleep(3)
    finally:
        release_lock()
        print("Lock released")

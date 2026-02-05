import os
import time

def watch_file(file_path, interval=2):
    last_modified = os.path.getmtime(file_path)

    while True:
        time.sleep(interval)
        current_modified = os.path.getmtime(file_path)
        if current_modified != last_modified:
            print("File changed!")
            last_modified = current_modified


if __name__ == "__main__":
    watch_file("example.txt")

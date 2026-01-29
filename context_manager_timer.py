import time

class Timer:
    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.end = time.time()
        print(f"Elapsed time: {self.end - self.start:.4f} seconds")


if __name__ == "__main__":
    with Timer():
        time.sleep(1.5)

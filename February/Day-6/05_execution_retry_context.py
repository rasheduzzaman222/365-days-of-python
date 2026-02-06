import time

class RetryContext:
    def __init__(self, retries=3, delay=1):
        self.retries = retries
        self.delay = delay

    def __enter__(self):
        return self

    def run(self, func):
        for attempt in range(self.retries):
            try:
                return func()
            except Exception as e:
                print(f"Attempt {attempt + 1} failed: {e}")
                time.sleep(self.delay)
        raise RuntimeError("All attempts failed")

    def __exit__(self, exc_type, exc, tb):
        return False


if __name__ == "__main__":
    def unstable():
        raise ValueError("fail")

    with RetryContext() as retry:
        retry.run(unstable)

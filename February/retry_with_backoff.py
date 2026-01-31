import time
import random

def retry_with_backoff(func, max_attempts=5):
    delay = 1

    for attempt in range(max_attempts):
        try:
            return func()
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)
            delay *= 2

    raise Exception("All retry attempts failed")


def unstable_operation():
    if random.random() < 0.7:
        raise ValueError("Random failure")
    return "Success"


if __name__ == "__main__":
    print(retry_with_backoff(unstable_operation))

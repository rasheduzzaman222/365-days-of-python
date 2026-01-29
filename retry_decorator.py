import time

def retry(max_attempts=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    print(f"Retry {attempts}/{max_attempts} failed: {e}")
                    time.sleep(delay)
            raise Exception("Max retry attempts reached")
        return wrapper
    return decorator


@retry(max_attempts=3, delay=2)
def unstable_function():
    raise ValueError("Temporary failure")


if __name__ == "__main__":
    unstable_function()

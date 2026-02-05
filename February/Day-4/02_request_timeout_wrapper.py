import signal

class TimeoutException(Exception):
    pass

def timeout(seconds):
    def decorator(func):
        def handler(signum, frame):
            raise TimeoutException("Operation timed out")

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, handler)
            signal.alarm(seconds)
            try:
                return func(*args, **kwargs)
            finally:
                signal.alarm(0)
        return wrapper
    return decorator


@timeout(2)
def slow_task():
    import time
    time.sleep(5)


if __name__ == "__main__":
    try:
        slow_task()
    except TimeoutException as e:
        print(e)

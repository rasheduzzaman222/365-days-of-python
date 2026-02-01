import time

class CircuitBreaker:
    def __init__(self, failure_threshold=3, recovery_time=5):
        self.failure_threshold = failure_threshold
        self.recovery_time = recovery_time
        self.failures = 0
        self.last_failure_time = None
        self.state = "CLOSED"

    def call(self, func):
        if self.state == "OPEN":
            if time.time() - self.last_failure_time > self.recovery_time:
                self.state = "HALF_OPEN"
            else:
                raise Exception("Circuit is open")

        try:
            result = func()
            self.failures = 0
            self.state = "CLOSED"
            return result
        except Exception:
            self.failures += 1
            self.last_failure_time = time.time()
            if self.failures >= self.failure_threshold:
                self.state = "OPEN"
            raise


def unstable_service():
    raise RuntimeError("Service down")


if __name__ == "__main__":
    cb = CircuitBreaker()
    try:
        cb.call(unstable_service)
    except Exception as e:
        print(e)

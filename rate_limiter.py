import time

class RateLimiter:
    def __init__(self, max_calls, period):
        self.max_calls = max_calls
        self.period = period
        self.calls = []

    def allow_request(self):
        now = time.time()
        self.calls = [t for t in self.calls if now - t < self.period]

        if len(self.calls) < self.max_calls:
            self.calls.append(now)
            return True
        return False


if __name__ == "__main__":
    limiter = RateLimiter(3, 5)

    for i in range(6):
        if limiter.allow_request():
            print("Request allowed")
        else:
            print("Rate limit exceeded")
        time.sleep(1)


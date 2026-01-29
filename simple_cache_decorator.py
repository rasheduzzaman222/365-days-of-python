def simple_cache(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            print("Fetching from cache...")
            return cache[args]

        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@simple_cache
def slow_add(a, b):
    print("Calculating...")
    return a + b


if __name__ == "__main__":
    print(slow_add(2, 3))
    print(slow_add(2, 3))

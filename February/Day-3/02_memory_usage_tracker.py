import tracemalloc

def track_memory(func):
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        result = func(*args, **kwargs)
        current, peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        print(f"Current: {current / 1024:.2f}KB, Peak: {peak / 1024:.2f}KB")
        return result
    return wrapper


@track_memory
def allocate():
    data = [i for i in range(100000)]
    return data


if __name__ == "__main__":
    allocate()

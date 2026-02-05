class LazyLoader:
    def __init__(self):
        self._data = None

    @property
    def data(self):
        if self._data is None:
            print("Loading data...")
            self._data = [i * i for i in range(10)]
        return self._data


if __name__ == "__main__":
    obj = LazyLoader()
    print(obj.data)
    print(obj.data)

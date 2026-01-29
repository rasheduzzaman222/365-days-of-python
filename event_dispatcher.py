class EventDispatcher:
    def __init__(self):
        self.listeners = {}

    def subscribe(self, event_name, callback):
        self.listeners.setdefault(event_name, []).append(callback)

    def dispatch(self, event_name, data=None):
        for callback in self.listeners.get(event_name, []):
            callback(data)


def on_user_created(data):
    print(f"User created: {data}")


if __name__ == "__main__":
    dispatcher = EventDispatcher()
    dispatcher.subscribe("user_created", on_user_created)
    dispatcher.dispatch("user_created", {"id": 1, "name": "Alice"})

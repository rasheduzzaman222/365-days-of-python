import uuid

def generate_request_id():
    return str(uuid.uuid4())


if __name__ == "__main__":
    print(generate_request_id())

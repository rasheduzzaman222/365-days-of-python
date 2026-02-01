import hashlib

def generate_checksum(file_path):
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        for chunk in iter(lambda: file.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


if __name__ == "__main__":
    print(generate_checksum("example.txt"))

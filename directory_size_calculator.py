import os

def get_directory_size(path):
    total_size = 0

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)

    return total_size


if __name__ == "__main__":
    folder = "."
    size = get_directory_size(folder)
    print(f"Directory size: {size / (1024 ** 2):.2f} MB")

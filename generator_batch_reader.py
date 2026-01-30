def read_in_batches(file_path, batch_size=3):
    with open(file_path) as file:
        batch = []
        for line in file:
            batch.append(line.strip())
            if len(batch) == batch_size:
                yield batch
                batch = []
        if batch:
            yield batch


if __name__ == "__main__":
    for chunk in read_in_batches("data.txt"):
        print(chunk)

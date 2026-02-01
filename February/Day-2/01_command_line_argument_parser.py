import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Simple CLI utility")
    parser.add_argument("--name", required=True, help="User name")
    parser.add_argument("--age", type=int, help="User age")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(f"Name: {args.name}, Age: {args.age}")

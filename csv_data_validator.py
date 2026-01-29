import csv

def validate_csv(file_path, required_fields):
    errors = []

    with open(file_path, newline="") as file:
        reader = csv.DictReader(file)
        for row_num, row in enumerate(reader, start=1):
            for field in required_fields:
                if not row.get(field):
                    errors.append(f"Row {row_num}: Missing '{field}'")

    return errors


if __name__ == "__main__":
    fields = ["id", "name", "email"]
    print(validate_csv("data.csv", fields))

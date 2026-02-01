def validate_json(data, schema):
    errors = []

    for key, expected_type in schema.items():
        if key not in data:
            errors.append(f"Missing key: {key}")
        elif not isinstance(data[key], expected_type):
            errors.append(f"Invalid type for key: {key}")

    return errors


if __name__ == "__main__":
    schema = {"id": int, "name": str}
    payload = {"id": 1, "name": "Alice"}

    print(validate_json(payload, schema))

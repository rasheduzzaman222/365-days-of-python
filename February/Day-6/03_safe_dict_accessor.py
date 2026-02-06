def deep_get(dictionary, keys, default=None):
    current = dictionary
    for key in keys:
        if isinstance(current, dict) and key in current:
            current = current[key]
        else:
            return default
    return current


if __name__ == "__main__":
    data = {"user": {"profile": {"email": "a@b.com"}}}
    print(deep_get(data, ["user", "profile", "email"]))

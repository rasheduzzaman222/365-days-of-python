import hmac

VALID_KEYS = {"abc123", "def456"}

def is_valid_api_key(key):
    for valid in VALID_KEYS:
        if hmac.compare_digest(key, valid):
            return True
    return False


if __name__ == "__main__":
    print(is_valid_api_key("abc123"))

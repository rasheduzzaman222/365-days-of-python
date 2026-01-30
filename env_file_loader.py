def load_env(file_path=".env"):
    env_vars = {}

    with open(file_path) as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            key, value = line.split("=", 1)
            env_vars[key.strip()] = value.strip()

    return env_vars


if __name__ == "__main__":
    print(load_env())

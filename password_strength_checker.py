import re

def check_password_strength(password):
    rules = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "digit": bool(re.search(r"\d", password)),
        "special_char": bool(re.search(r"[!@#$%^&*()]", password)),
    }

    strength = sum(rules.values())

    if strength == 5:
        return "Strong Password"
    elif strength >= 3:
        return "Medium Password"
    else:
        return "Weak Password"


if __name__ == "__main__":
    pwd = input("Enter password: ")
    print(check_password_strength(pwd))

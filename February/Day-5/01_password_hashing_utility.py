import bcrypt

def hash_password(password: str) -> bytes:
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode(), salt)

def verify_password(password: str, hashed: bytes) -> bool:
    return bcrypt.checkpw(password.encode(), hashed)


if __name__ == "__main__":
    hashed_pwd = hash_password("secure123")
    print(verify_password("secure123", hashed_pwd))

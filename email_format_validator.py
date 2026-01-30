import re

EMAIL_REGEX = r"^[\w\.-]+@[\w\.-]+\.\w+$"

def is_valid_email(email):
    return bool(re.match(EMAIL_REGEX, email))


if __name__ == "__main__":
    emails = ["test@mail.com", "invalid@", "user@domain.org"]
    for email in emails:
        print(email, is_valid_email(email))

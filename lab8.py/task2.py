import re

def is_valid_email(email):
    # Check for exactly one '@'
    if email.count('@') != 1:
        return False
    # Email must not start or end with special characters
    if re.match(r'^[^a-zA-Z0-9]', email) or re.match(r'.*[^a-zA-Z0-9]$', email):
        return False
    # Basic pattern: at least one character before and after '@'
    if not re.match(r'^[a-zA-Z0-9][\w\.-]@[a-zA-Z0-9][\w\.-]\.[a-zA-Z]{2,}$', email):
        return False
    return True

def main():
    email = input("Enter your email: ")
    if is_valid_email(email):
        print("Valid email.")
    else:
        print("Invalid email.")

if __name__== "__main__":
    main()
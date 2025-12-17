# auth.py
# Handles user authentication for the system

VALID_USERNAME = "user123"
VALID_PASSWORD = "Givemetheykey123"
MAX_ATTEMPTS = 3

def authenticate_user():
    """
    Authenticates a user by checking username and password.
    Allows a maximum of three failed attempts.
    """
    attempts = 0

    while attempts < MAX_ATTEMPTS:
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username == VALID_USERNAME and password == VALID_PASSWORD:
            print("\nLogin successful!\n")
            return True
        else:
            attempts += 1
            remaining = MAX_ATTEMPTS - attempts
            print(f"Invalid credentials. Attempts remaining: {remaining}")

    print("\nToo many failed attempts.")
    print("Account locked for 5 minutes. Please try again later.\n")
    return False

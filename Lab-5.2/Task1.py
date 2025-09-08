import os
import hashlib
import getpass

# Insecure logic example (for review)
def insecure_login(username, password):
    # Hardcoded password (bad practice)
    if username == "admin" and password == "password123":
        return True
    return False

# Secure logic with password hashing and environment variable
def hash_password(password):
    # Use SHA-256 for hashing (better to use bcrypt or argon2 in production)
    return hashlib.sha256(password.encode()).hexdigest()

def secure_login(username, password):
    # Get hashed password from environment variable
    stored_hash = os.environ.get("ADMIN_PASSWORD_HASH")
    if not stored_hash:
        print("Admin password hash not set in environment variable.")
        return False
    # Compare hashes
    return username == "admin" and hash_password(password) == stored_hash

if __name__ == "__main__":
    print("Login System")
    username = input("Username: ")
    password = getpass.getpass("Password: ")

    # Insecure check
    if insecure_login(username, password):
        print("Insecure login: Access granted!")
    else:
        print("Insecure login: Access denied.")

    # Secure check
    if secure_login(username, password):
        print("Secure login: Access granted!")
    else:
        print("Secure login: Access denied.")

# To set up the environment variable for secure login:
# import os, hashlib
# os.environ["ADMIN_PASSWORD_HASH"] = hashlib.sha256("your_secure_password".encode()).hexdigest()
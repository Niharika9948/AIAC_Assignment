def register_user(users, username, password):
    if username in users:
        print(f"Registration failed: Username '{username}' already exists.")
        return False  # Username already exists
    users[username] = password
    print(f"Registration successful for user '{username}'.")
    return True  # Registration successful

def login_user(users, username, password):
    if username in users and users[username] == password:
        print(f"Login successful for user '{username}'.")
        return True  # Login successful
    else:
        print(f"Login failed for user '{username}'. Invalid username or password.")
        return False  # Invalid username or password

# Example usage:
users = {}
# Register a user
register_user(users, "alice", "password123")
# Try to login
login_success = login_user(users, "alice", "password123")



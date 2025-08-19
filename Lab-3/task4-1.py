def register_user(users):
    username = input("Enter a new username: ")
    if username in users:
        print("Username already exists. Please try a different one.")
        return False
    password = input("Enter a new password: ")
    users[username] = password
    print("Registration successful!")
    return True

def login_user(users):
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

# Example usage:
if __name__ == "__main__":
    users = {}
    while True:
        print("\n1. Register\n2. Login\n3. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            register_user(users)
        elif choice == "2":
            login_user(users)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


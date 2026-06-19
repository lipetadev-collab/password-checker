import secrets
import string

def check_strength(password):
    symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in symbols for c in password)
    
    score = 0
    if len(password) >= 8:
        score += 1
    if len(password) >= 12:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_symbol:
        score += 1
    
    return score


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    new_password = "".join(secrets.choice(characters) for _ in range(length))
    return new_password


def is_common_password(password):
    with open("common_passwords.txt", "r") as file:
        common_passwords = file.read().splitlines()
    return password in common_passwords


while True:
    print("\n1 - Check password strength")
    print("2 - Generate a strong password")
    print("3 - Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        password = input("Type a password to check: ")

        if is_common_password(password):
            print("This password is in a list of commonly leaked passwords! 🔴")
        else:
            score = check_strength(password)
            print("Score:", score, "out of 6")
            if score <= 2:
                print("WEAK password 🔴")
            elif score <= 4:
                print("MEDIUM password 🟡")
            else:
                print("STRONG password 🟢")
    elif choice == "2":
        length = input("How many characters? (default 12): ")
        
        if length == "":
            new_password = generate_password()
        else:
            new_password = generate_password(int(length))
        
        print("Your new password:", new_password)
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid option.")
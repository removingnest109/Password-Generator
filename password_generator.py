import os
import sys

def generate_password(password_length):
    password = ''
    while len(password) < password_length:
        new_character = chr(ord(os.urandom(1)))
        if new_character in '()!@#$%&*?<>/^-_=+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890':
            password += new_character
    return password

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <password_length>")
        sys.exit(1)

    try:
        password_length = int(sys.argv[1])
    except ValueError:
        print("Error: Password length must be an integer.")
        sys.exit(1)

    if password_length <= 0:
        print("Error: Password length must be greater than 0.")
        sys.exit(1)

    password = generate_password(password_length)
    print(password)

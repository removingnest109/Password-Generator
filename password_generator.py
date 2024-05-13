import os

password_length = 16
password = ''

while len(password) < password_length:
    new_character = chr(os.urandom(1)[0])
    if new_character in '()!@#$%&*?<>/^-_=+qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890':
        password += new_character

print(password)

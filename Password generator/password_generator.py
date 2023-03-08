import random
import os
import string

password_length = 16

per_type = int(password_length / 4)
leftover = password_length - per_type * 3
uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase
digits = string.digits
symbols = '()!@#$%&*/?'

password = ''.join(
    [random.choice(uppercase_letters) for _ in range(per_type)] + 
    [random.choice(digits) for _ in range(per_type)] +
    [random.choice(symbols) for _ in range(per_type)] +
    [random.choice(lowercase_letters) for _ in range(leftover)])

desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
with open(os.path.join(desktop_path, 'output.txt'), 'w') as file:
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)
    file.write(password)

os.startfile(os.path.join(desktop_path, 'output.txt'))
import os
import string
import configparser
config_file = 'config.ini'
if not os.path.isfile(config_file):
    # generate config file
    config = configparser.ConfigParser()
    config['keys'] = {'password_length': 16}
    with open(config_file, 'w') as f:
        config.write(f)
config = configparser.ConfigParser()
config.read(config_file)
password_length = int(config.get('keys', 'password_length'))
allowed_chars = string.ascii_letters + string.digits + '()!@#$%&*?'
password = ''
while len(password) < password_length:
    char = chr(os.urandom(1)[0])
    if char in allowed_chars:
        password += char
output_path = os.getcwd()
with open(os.path.join(output_path, 'output.txt'), 'w') as file:
    file.write(password)
os.startfile(os.path.join(output_path, 'output.txt'))

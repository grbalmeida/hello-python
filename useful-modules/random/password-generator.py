import random
import string

letters = string.ascii_letters
print(letters)

digits = string.digits
print(digits)

characters = '!@#$%&._-'

all = letters + digits + characters
password = ''.join(random.choices(all, k=20))
print(password)

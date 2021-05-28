import random
import string
import hashlib

abc = [le for le in string.ascii_letters]
num = [num for num in string.digits]
sym = ['@', '*', '#', '!', '%', '.', ',']


desired_len = input("What is the size of the password you want to generate? Enter a number (1-65):\n")

try:
    desired_len = int(desired_len)
    success = 1
except ValueError:
    success = None

while success is None:
    print('Invalid Number!')
    desired_len = input("What is the size of the password you want to generate? Enter a number (1-65):\n")
    try:
        desired_len = int(desired_len)
        success = 1
    except ValueError:
        success = None

as_set = set()

while len(as_set) < desired_len:
    _type = random.choice([abc, num, sym])
    char = random.choice(_type)

    as_set.add(char)


password = ''.join(as_set)

with open('passwords.txt', 'a') as file:
    file.write(f"{as_set}\n")


print(f"Your password: {password}\n")

import random

letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "1234567890"
symbols = "~!@#$%^&*()+-"

print("Welcome to the Python Password Generator")
num_letters = int(input("How many letters do you want in your password?\n"))
num_numbers = int(input("How many numbers do you want in your password?\n"))
num_symbols = int(input("How many symbols do you want in your password?\n"))

password = ""

for n in range(1,num_letters+1):
    cap = random.choice([0,1])
    print(cap)
    if cap == 1:
        password += random.choice(letters).capitalize()
    else:
        password += random.choice(letters)
for n in range(1,num_numbers+1):
    password += random.choice(numbers)
for n in range(1,num_symbols+1):
    password += random.choice(symbols)


password = list(password)
random.shuffle(password)
password = ''.join(password)
print(password)
import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
number = random.choice(range(1,1001))
num_guess = 10
game_end = False

diff = input("Choose a difficulty. Type 'easy' or 'hard': ")
if diff == "hard":
    num_guess = 5
print(f"You have {num_guess} attempts reamining to guess the number.\n")
print(f"The number is {number}.")
while not game_end and num_guess > 0:

    guess = int(input("Make a guess: "))

    if guess > number:
        print("Too high.\nGuess again.\n")
        num_guess -= 1
        print(f"You have {num_guess} attempts reamining to guess the number.\n")

    elif guess < number:
        print("Too low.\nGuess again.\n")
        num_guess -= 1
        print(f"You have {num_guess} attempts reamining to guess the number.\n")


print(f"Sorry! The number was {number}.")
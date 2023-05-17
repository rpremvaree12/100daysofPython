import random
from colorama import Fore, Back, Style
import art
 #todo add colors to output using colorama
 # add in ascii images of rock paper scissors


print("Let's play a game of Rock Paper Scissors!")
userchoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. "))
computerchoice = random.randint(0,2)

rps = ["Rock","Paper","Scissors"]

score = userchoice - computerchoice

if score == 0:
    print(f"\nYou chose {rps[userchoice]}. {art.rps[userchoice]} \nThe computer chose {rps[computerchoice]}. {art.rps[computerchoice]}")
    print("It's a tie.")
elif score == 1 or score == -2:
    print(f"You chose {rps[userchoice]}.{art.rps[userchoice]} \nThe computer chose {rps[computerchoice]}.{art.rps[computerchoice]}")
    print("You WIN.")
elif score == -1 or score == 2:
    print(f"\nYou chose {rps[userchoice]}.{art.rps[userchoice]}\nThe computer chose {rps[computerchoice]}.{art.rps[computerchoice]}")
    print("You LOSE.")
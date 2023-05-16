import random
import art
from game_data import data


score = 0
should_continue = True

while should_continue:
    opt_a = data[random.choice(range(1,len(data)))]
    opt_b = data[random.choice(range(1,len(data)))]


    print(f"Compare A: {opt_a['name']}, a {opt_a['description']}, from {opt_a['country']}")
    print(art.vs)
    print(f"Against B: {opt_b['name']}, a {opt_b['description']}, from {opt_b['country']}")

    choice = input("Which Instagram account has more followers? Type 'A' or 'B' ").upper()
    print(chr(27) + "[2J")

    if choice == "A" and opt_a['follower_count'] > opt_b['follower_count']:
        score += 1
        should_continue = True
        print(art.logo)
        print(f"You're right! Current score: {score}")
    
    elif choice == "B" and opt_a['follower_count'] < opt_b['follower_count']:
        score += 1
        should_continue = True
        print(art.logo)
        print(f"You're right! Current score: {score}")

    else:
        should_continue = False
        print(art.logo)
        print(f"Sorry. That's wrong.\n{opt_a['name']} has {opt_a['follower_count']} followers and \n{opt_b['name']} has {opt_b['follower_count']} followers\n")
        print(f"Final score: {score}\n")
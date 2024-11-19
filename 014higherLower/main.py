import random
import json
import art
from game_data import data as game_data
#TODO: add in real data
with open("db.json","r") as database:
    db = json.load(database)
    high_scores ={
    "score": db["score"],
    "name": db["name"]
    }
database.close()

score = 0
should_continue = True

while should_continue:
    opt_a = game_data[random.choice(range(1,len(game_data)))]
    opt_b = game_data[random.choice(range(1,len(game_data)))]

    #check if the chosen are the same.
    if opt_a['name'] != opt_b['name']:

        print(art.logo)
        print(f"Compare A: {opt_a['name']}, a {opt_a['description']}, from {opt_a['country']}")
        print(art.vs)
        print(f"Against B: {opt_b['name']}, a {opt_b['description']}, from {opt_b['country']}")

        choice = input("Which Instagram account has more followers? Type 'A' or 'B' ").upper()
        
        #clear the screen
        print(chr(27) + "[2J")

        if choice == "A" and opt_a['follower_count'] > opt_b['follower_count']:
            score += 1
            should_continue = True
            print(f"You're Right! {opt_a['name']} has {opt_a['follower_count']},000 followers and \n{opt_b['name']} has {opt_b['follower_count']},000 followers\n")
            print(f"You're right! Current score: {score}")
        
        elif choice == "B" and opt_a['follower_count'] < opt_b['follower_count']:
            score += 1
            should_continue = True
            print(f"You're Right! {opt_a['name']} has {opt_a['follower_count']},000 followers and \n{opt_b['name']} has {opt_b['follower_count']},000 followers\n")
            print(f"You're right! Current score: {score}")

        else:
            should_continue = False
            print(f"Sorry. That's wrong.\n{opt_a['name']} has {opt_a['follower_count']},000 followers and \n{opt_b['name']} has {opt_b['follower_count']},000 followers\n")
            print(f"Final score: {score}\n")

if score > high_scores["score"]:
    print("You've achieved a high score!")
    high_scores["score"] = score
    high_scores["name"] = input("Enter your name: ")
    with open("db.json","w") as db:
        json.dump(high_scores, db)
    db.close()


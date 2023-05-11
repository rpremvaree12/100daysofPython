import art
import random

'''
Blackjack - unlimited cards, only 1 player vs. dealer.
1. deal 2 cards to each person. only show first card of dealer.
2. give option to hit or stay.
3. if above 21, player loses    
4. if stays, dealer shows second card. if less than 17, has to hit.
5. check player and dealer total. higher total wins unless bust.


features: double, split, insurance if dealer has ace, betting option
'''

player_cards = []
dealer_cards = []
bankroll = 1000

def gameStart():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for n in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    displayHand(player_cards)
    print(f"\tDealer's first card is: {dealer_cards[0]}.\n")
    return

def dealToPlayer(action):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if action == "hit" or action == "double":
        player_cards.append(random.choice(cards))
        displayHand(player_cards)
        return
    
def dealToDealer():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    print("Dealer's turn.\n")
    while handTotal(dealer_cards) <= 16:
        print("Dealer hits.\n")
        dealer_cards.append(random.choice(cards))
        displayHand(dealer_cards)
    if handTotal(dealer_cards) > 21:
        print("Dealer busts.\n")
        return True
    else:
        print(f"dealer: {handTotal(dealer_cards)} player: {handTotal(player_cards)}")
        return handTotal(dealer_cards) < handTotal(player_cards)

def displayHand(cards):
    if cards == player_cards:
        print(f"\tYour cards: {cards}.\n\tYou have: {handTotal(player_cards)}\n")
        return
    elif cards == dealer_cards:
        print(f"\tDealer's cards are {cards},\n \tDealer has: {handTotal(dealer_cards)}\n")
        return
    else:
        return

def handTotal(hand):
    total = 0
    for c in hand:
        total += c
    if 11 in hand and total > 21:
        total -= 10
    return total
    

# game start section
print(art.logo)
print("Welcome to Python BlackJack.")
play = input("Would you like to play? 'y' or 'n'?\n")
if play.lower()[0] == 'y':
    bet = int(input(f"Your current bankroll is ${bankroll}. Place your bet.\n$"))
    gameStart()

player_end = False
while not player_end:

    ##check if player has blackjack - add to 21 and 2 cards
    if handTotal(player_cards) == 21 and len(player_cards) == 2:
        if handTotal(dealer_cards) == 21:
            print("Push! Dealer has Blackjack.")
            displayHand(dealer_cards)

        else:
            bankroll += 1.5 * bet
            player_end = True
            print("Blackjack!")
            print(f"Your bankroll is now ${bankroll}.")

    #player does not have black jack        
    else:
        
        action = input("Would you like to hit, stay or double?\n")
        if action == "hit":
            dealToPlayer("hit")

        elif action == "stay":
            player_end = True

            #deal to the dealer
            if dealToDealer():
                print("You win.")

            else:
                print("You lose.")

        # elif action == "double":
        #     dealToPlayer("double")
        #     bet *= 2
        #     player_end = True
            
        #     #deal to the dealer
        #     if dealToDealer():
        #         print("You win.")

        #     else:
        #         print("You lose.")

        if handTotal(player_cards) > 21:
            displayHand(dealer_cards)
            print("Bust! You lose.\n")
            bankroll -= bet
            player_end = True
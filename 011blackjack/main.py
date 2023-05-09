import art
import random

'''
Blackjack - unlimited cards, only 1 player vs. dealer.
1. deal 2 cards to each person. only shows first card of dealer.
2. give option to hit or stay.
3. if above 21, player loses    
4. if stays, dealer shows second card. if less than 17, has to hit.
5. check player and dealer total. higher total wins unless bust.


features: double, split, insurance if dealer has ace, betting option
'''

player_cards = []
dealer_cards = []
bankroll = 1000

def dealToPlayer(action):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    if action =="stay":
        return
    elif action == "hit":
        player_cards.append(random.choice(cards))
        return
    elif action == "double":
        player_cards.append(random.choice(cards))
        return

def gameStart():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    for n in range(2):
        player_cards.append(random.choice(cards))
        dealer_cards.append(random.choice(cards))
    return

def displayHand(cards):
    if cards == player_cards:
        print(f"\tYour cards are {cards}. Total: {handTotal(player_cards)}")
    if cards == dealer_cards and action == "stay":
        print(f"\tYour cards are {cards}. Total: {handTotal(player_cards)}")


def handTotal(hand):
    handTotal = 0
    for c in hand:
        handTotal += c
    return handTotal

print(art.logo)
print("Welcome to Python BlackJack.")
play = input("Would you like to play? 'y' or 'n'?\n")
if play.lower()[0] == 'y':
    bet = int(input("Place your bet.\n$"))

    print(dealToPlayer("deal"))
    dealToDealer("deal")

print(f"\tDealer's first card is: {dealer_cards[0]}")

game_end = False
while not game_end:
    if handTotal(player_cards) == 21:
        print("Blackjack!")
        bankroll += 1.5 * bet
    else:
        action = input("Would you like to hit, stay or double?\n")
    dealToPlayer(action)
    displayPlayerHand()


    if handTotal(player_cards) > 21:
        print("Bust! You lose.")
        game_end = True
        bankroll -= bet
    elif handTotal(dealer_cards) > 21 or handTotal(player_cards) > handTotal(dealer_cards):
        game_end = True
        print("You win.")
        bankroll += bet
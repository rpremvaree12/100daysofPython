import art

print(art.logo)

end_auction = False
auction = {}
while not end_auction:
    name = input("What is your name? ").lower()
    bid = int(input("What's your bid? $"))
    done = input("Are there any other bidders? Type 'yes' or 'no' ").lower()

    auction[name] = bid

    if done == "yes":
        #clear the screen
        print(chr(27) + "[2J")
    else:
        break

high_bid = 0
bidder = ""
for n in auction:
    if auction[n] > high_bid:
        high_bid = auction[n]
        bidder = n
print(f"The winner of the auction is {bidder.capitalize()} with a bid of ${high_bid}")

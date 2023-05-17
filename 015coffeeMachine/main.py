# TODOs
# print out a report of water, milk, coffee and money by entering "report"
# turn machine off by entering "off"
# check if resources are sufficient and produces change
# process coins
# check if transaction is successful
# make coffee - deduct resources
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

denom = {
    "quarter": 0.25,
    "dime": 0.10,
    "nickel": 0.05,
    "penny": 0.01
}

def report():
    for item in resources: 
        if item == "water" or item == "milk":
            print(f"{item}: {resources[item]} ml")
        elif item == "coffee":
            print(f"{item}: {resources[item]} g")
        elif item == "money":
            print(f"{item}: ${resources[item]}")
    return

def check_resources(bev):
    for r in resources:
        if r in MENU[bev]["ingredients"] and (resources[r] - MENU[bev]["ingredients"][r]) < 0:
            print(f"Not enough {r} to make {bev}")
            return False
        return True

def collect_money():
    total = 0
    for c in denom:
        total += int(input(f"How many {c}s do you have? ")) * denom[c]
    return total


def make_drink(bev):
    if check_resources(bev):
        for r in resources:
            if r in MENU[bev]["ingredients"]:
                resources[r] -= MENU[bev]["ingredients"][r]
        print(f"Here's your {bev}! Enjoy!")
        return True
    else:
        return False

operating = True

while operating:
    bev = input("Would you like an espresso, latte or cappuccino? ").lower()
    if bev == "report":
        report()
    elif bev == "off":
        operating = False
    elif collect_money() - MENU[bev]["cost"] > 0:
        make_drink(bev)
        print("")
    else:
        print("Sorry, you don't have enough money.")

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
    "coffee": 100,
    "money": 0
}

def report():
    for item in resources: 
        if item == "water" or item == "milk" or item == "coffee":
            print(f"{item}: {resources[item]} ml")
    return

def process_coins():
    return

def check_resources(bev):
    return True

def make_coffee():
    return

report()
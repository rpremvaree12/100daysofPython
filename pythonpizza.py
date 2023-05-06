# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total = 15

match size.upper():
    case "L":
        total = 25
    case "M":
        total = 20
    case "S":
        total = 15


if add_pepperoni[0].upper() == "Y":
    total += 2
if extra_cheese[0].upper() == "Y":
    total += 1

print(total)

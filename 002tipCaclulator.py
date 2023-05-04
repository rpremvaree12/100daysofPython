
total = float(input("What is the total bill? $"))
num_people = int(input("How many people to split the bill? "))
tip_percent = float(input("What percentage tip would you like to give? 10, 12 or 15? "))/100

print(f"Each person should pay $ {round(total*(1+tip_percent)/num_people, 2)}")
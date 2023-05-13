# started 5/12/2023
# create a CL calulator that will allow the user to enter at least 2 numbers and an operation.
# the calculator will also prompt the user whether they want to continue the calculator or end it.
# if the user wants to continue, they will chain an operation to the previous result.
import art

def add(num1,num2):
    return num1 + num2

def sub(num1,num2):
    return num1 - num2

def mult(num1,num2):
    return num1 * num2

def div(num1,num2):
    return num1 / num2


print(art.logo)
print("Welcome to the Python Command Line Calculator.")
operations ={
    "+": add,
    "-": sub,
    "*": mult,
    "/": div
}


calc_end = False

first_num = float(input("What's the first number in your calculation? "))
op = input("Pick an operation: ")
next_num = float(input("What's the next number in the calculation? "))
result = operations[op](first_num, next_num)

print(f"{first_num} {op} {next_num} = {result}")

while not calc_end:
    cont = input("Would you like to continue? 'y' for yes 'n' for no.")
    if cont == "y":
        first_num = result
        next_num = float(input("What's the next number in the calculation? "))





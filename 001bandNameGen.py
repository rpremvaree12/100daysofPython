# simple band name generator based on user input

# 1. Create  a greeting for your program
# 2. Ask the user for the city that they grew up in
# 3. Ask the user for their pet's name
# 4. Combine the name of their city and pet's name
# 5. Make sure the input cursor shows on a new license

print("Welcome to the Band Name Generator!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What's your pet's name?\n")

print("Your band name could be",city.capitalize(),pet.capitalize())

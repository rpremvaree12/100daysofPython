# try: something that might cause an exception
# except: do this if there was an exception
# else: do this if there were no execeptions
# finally: do this no matter what happens
# raise: create your own exception

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     # open in write mode - creates a new file
#     file = open("a_file.txt","w")
#     file.write("Something")
#     # except: just by itself - too broad
# except KeyError as error_message:
#     # capture key error in variable
#     print(f"The key {error_message} doesn't exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed")

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be larger than 3 meters")

bmi = height / (weight**2)
print(bmi)
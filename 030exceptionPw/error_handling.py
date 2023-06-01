# try: something that might cause an execetion
# except: do this if there was an exception
# else: do this if there were no execeptions
# finally: do this no matter what happens

# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    print(a_dictionary["asdf"])
except FileNotFoundError:
    # open in write mode - creates a new file
    file = open("a_file.text","w")
    # except: just by itself - too broad
except KeyError as error_message:
    # capture key error in variable
    print(f"The key {error_message} doesn't exist.")

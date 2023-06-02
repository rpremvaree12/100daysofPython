import pandas as pd


#TODO 1. Create a dictionary in this format:
nato_df = pd.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter:row.code for (index, row) in nato_df.iterrows()}

def generate_phonetic():
    phrase = input("Enter the phrase you wish to translate: ")
    try:
        nato_words = [nato_dict[c.upper()] for c in phrase]
    except KeyError as error_message:
        print(f"Sorry, only letters in the alphabet please!")
        generate_phonetic()
    else:
        print(nato_words)


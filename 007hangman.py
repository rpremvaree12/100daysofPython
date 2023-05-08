"""
1. chose a random word
2. display how many letters in the word with blanks
3. show how many guesses user has
4. when a user guesses a letter check if the letter is in the word.
prevent the user from selecting the same letter or a nonletter. the letter case does not matter
    if it is, show the all of the places where the letter is
    if it isnt, draw a piece of the hangman
5. if there are no more missing letters, the user wins
    if all pieces of the hangman are drawn, the user loses

"""


#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print("chosen word is",chosen_word)
#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
for c in chosen_word:
    if c == guess:
        print("Found!")
    else:
        print("Not in the word")
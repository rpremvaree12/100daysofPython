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

import random
import hangman_art
import hangman_words
word_list = hangman_words.word_list

# ASCII art list for lives. The user starts with 6 lives. art corresponds with num lives
lives = 6


# choose a random word
chosen_word = random.choice(word_list).lower()
word_length = len(chosen_word)
print("chosen word is",chosen_word)
print(hangman_art.logo)

# create a list of empty blanks for every letter in the chosen word
display = []
for c in chosen_word:
    display.append("_")


# play the game until end game is triggered - 0 lives or no blanks
end_of_game = False
guessed_letters = ""
while not end_of_game:
    guess = input("Guess a letter\n").lower()
    found_letter = False

    if guess not in guessed_letters:
        guessed_letters += guess

        for pos in range(word_length):
            if chosen_word[pos] == guess:
                display[pos] = guess
                found_letter = True
    
        if found_letter == False:
            lives -= 1
            print(f"Sorry. {guess} is not in the word. You lost a life. {lives} lives left.")
        
        # show ASCII art based on their current lives
        print(hangman_art.stages[lives])

    else:
        print(f"You've already guessed the letter {guess}. Try again.")

    # display the blanks and already guessed letters
    print(" ".join(display))

    if "_" not in display or lives == 0:
        end_of_game = True
    
if lives == 0:
    print(f"No more lives left. You lose. The word was {chosen_word}")
else:
    print("You win!")
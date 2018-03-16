# !/usr/bin/env python

"""
A game of guess the word.
Users will get seven guesses (size of the man) to correctly guess the random word from the words.  Game includes:

* Functions
* Lists and
* Error checking
* DocStrings
* If/else statements

When the script runs it will call for user input to enter a letter.  Letters that match the new random word will replace
dashed word with letter.  Wrong letters will print another progression of the man.

"""
import random  # used for generated random word from word list
import string  # used for validating user input against the alphabet
import sys  # for system exit

# GLOBALS AND CONSTANTS
# words that will be used for the game
words = ['python', 'module', 'canvas', 'github', 'pseudocode', 'pycharm', 'jupyter', 'pandas']
new_word = random.choice(words).lower()  # generates a new random word from the word list for each new game
length_word = len(new_word)  # calculates the length of the new word
word_listed = list(new_word)  # separates random word into individual chars
get_dash = []  # empty list for random word's letters
get_dash.extend(word_listed)  # add new word's letters to get_dash list
guesses_taken = 0 # track number of guesses.  If guesses_taken = secret word length, the user is a winner
max_guesses = 7 # needed to display word



def intro():
    """game introduction"""
    print(
        '\nLet\'s play Guess the Word! \n\nA word will be chosen at random and you\'ll get seven guesses to try and answer it. \n'
        'Guess incorrectly seven times and you lose!  Are you ready?  Let\'s play! \n')


def get_dashed_word(get_dash):
    """ Convert the random word to dashes """
    for x in range(len(get_dash)):
        get_dash[x] = "_"


def get_word_length(length_word):
    print("The word you need to guess has {} ({}) characters".format(length_word, ' '.join(get_dash)))


def game(guesses_taken, get_dash, word_listed, max_guesses):
    guessed_letters = []
    while guesses_taken < len(word_listed):
        user_guess = input("\nEnter a letter: ").lower()

        for i in range(len(word_listed)):
            if word_listed[i] == user_guess and not word_listed[i] in guessed_letters:
                get_dash[i] = user_guess
                print("You guessed correctly! \n{}\n".format(" ".join(get_dash)))
                guessed_letters.append(user_guess)
                guesses_taken += 1
                break

            elif user_guess in guessed_letters:
                print("You have already guessed that letter!\n")
                break

            # verify that guess is in the alphabet
            elif not user_guess in string.ascii_letters:
                print("Sorry, you guess must be a letter.  Try again.\n")
                break

            elif not user_guess in word_listed:
                max_guesses -= 1
                guessed_letters.append(user_guess)
                print("\nOh no! That letter is not in the word. You have {} guesses remaining. You've inputted the"
                      " following letters already: {}. Try Again!".format(max_guesses, guessed_letters))
                find_word(max_guesses)
                break
    print("You won!  Nice work!!")


def find_word(max_guesses):
    if max_guesses == 6:
        print("\n    ^   \n")
    if max_guesses == 5:
        print("\n    ^   \n", "  0_0    \n")
    if max_guesses == 4:
        print("\n    ^   \n", "  0_0  \n", " __+__\n")
    if max_guesses == 3:
        print("\n    ^   \n", "  0_0  \n", " __+__\n", "/  |  \ \n")
    if max_guesses == 2:
        print("\n    ^   \n", "  0_0  \n", " __+__\n", "/  |  \ \n", "   |  \n")
    if max_guesses == 1:
        print("\n    ^   \n", "  0_0  \n", " __+__\n", "/  |  \ \n", "   |  \n", "  / \  \n")
    if max_guesses == 0:
        print("\n    ^   \n", "  0_0  \n", " __+__\n", "/  |  \ \n", "   |  \n", "  / \  \n", " /   \ \n\n",
              "\nGame over.  The boogeyman has manifested. The word was {}".format(new_word))
        sys.exit("Laters!")


if __name__ == '__main__':
    intro()
    get_dashed_word(get_dash)
    get_word_length(length_word)
    game(guesses_taken, get_dash, word_listed, max_guesses)

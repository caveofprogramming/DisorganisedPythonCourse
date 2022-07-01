#!./venv/bin/python

import random

class WordGame:
    def __init__(self, *words):

        # List of possible words
        self._words = words

        # Set of correctly-guessed letters
        self._guesses = set()

        # Set of all letters in the word
        self._letters = set()

        # Number of guesses made by the user
        self._number_guesses = 0

        self._word = None

    def _choose_word(self):
        self._word = random.choice(self._words)
        self._letters.update(self._word)

    def _guess_letter(self):
        # Ask the user to guess a letter
        # If the letter is in the chosen word, add it to self._guesses
        pass

    def run(self):
        self._show_word()

def main():
    game = WordGame('peach', 'alligator', 'sky', 'fascinate')
    game.run()
    
main()

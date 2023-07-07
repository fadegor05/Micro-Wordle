from config import *
from random import randint
from draw import Draw
import string

# Main game class
class Game:
    # Game init function
    def __init__(self):
        self.draw = Draw()
        # Start Main loop
        self.main_loop(self.pick_word(), ATTEMPTS)
    
    # Function that read wordlist and return it
    def read_wordlist(self):
        # Openning file with wordlist
        with open(WORDS_FILE) as f:
            # Getting words and cutting escape character if they are
            return [line.rstrip() for line in f]
        

    # Function that pick random word from wordlist
    def pick_word(self):
        # Return a random word from list
        return self.read_wordlist()[randint(0,len(self.read_wordlist())-1)]

    # Function that gets guesses
    def get_guess(self):
        # Get guessing loop
        while True:
            # Input the guess
            guess = input('>> ')
            # If wordlist contains guess
            if guess.lower() in self.read_wordlist(): 
                # Return if it is true
                return guess.lower()
            else:
                # If not go in loop again
                print('try again...')

    # Function that check does player entered right word
    def check_word(self, word, hidden_word):
        return True if word == hidden_word else False

    # Main loop function
    def main_loop(self, hidden_word, attempts):
        # Creating variable that counts attempts
        attempt = 0
        # Main loop
        while True:
            # Checking don't we run out of attempts
            if not attempt < attempts: 
                # If ran out of attempts
                print('your attempts are out :(')
                print(f'the word was: {hidden_word}')
                break

            # Guessing the word
            print(f'attempt {attempt+1}')
            current_word = self.get_guess()

            # Checking if word of player equals to hidden word
            if self.check_word(current_word, hidden_word):
                # If equals
                print('hooray')
                break

            # Adding attempt
            attempt += 1

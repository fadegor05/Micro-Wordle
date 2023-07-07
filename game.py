from config import *
from random import randint

# Main game class
class Game:
    # Game init function
    def __init__(self):
        pass
    
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

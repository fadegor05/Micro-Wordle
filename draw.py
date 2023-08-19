from config import *
from colorama import init, Fore, Style

# Main draw class
class Draw:
    def __init__(self):
        # Credentials
        print(f'\n{Fore.CYAN}Micro-Wordle{Style.RESET_ALL}')
        print(f'{Fore.CYAN}by Fadeev Egor{Style.RESET_ALL}\n')

    # Lost drawing function
    def lost(self, hidden_word):
        print(f'\n{Fore.YELLOW}You lost!{Style.RESET_ALL}')
        print(f'{Fore.CYAN}Word: {Style.RESET_ALL}{hidden_word}\n')

    # Win drawing function
    def win(self, hidden_word):
        print(f'\n{Fore.GREEN}You are right!{Style.RESET_ALL}')
        print(f'{Fore.CYAN}Word: {Style.RESET_ALL}{hidden_word}\n')

    def print_keyboard(self, symbols, categorized_symbols):
        print(f'{Style.RESET_ALL}')
        # Checking does alphabet letter equals to the word and parallel printing alphabet letters
        for letter in symbols:
            print( f'{Fore.GREEN}{letter} ' if letter in categorized_symbols["correct"] else f'{Fore.YELLOW}{letter} ' if letter in categorized_symbols["another_place"] else f'{Fore.BLACK}{letter} ' if letter in categorized_symbols["not_contain"] else f'{Fore.WHITE}{letter} ', end='')
        print(f'{Style.RESET_ALL}')

    # Main update function
    def update(self, attempt, guesses, hidden_word, symbols):
        categorized_symbols = {"correct" : [], "another_place": [], "not_contain": []}
        # Printing current attempt
        print(f'\n{Fore.CYAN}Attempt {Fore.WHITE}{attempt+1}\n')
        # Getting words from all guesses
        for x,word in enumerate(guesses):
            # Printing number of word
            print( f'{Fore.CYAN}{x+1}. ', end='')
            # Checking does letter equals to the word and parallel printing letters
            for n, letter in enumerate(word):
                print( f'{Fore.GREEN}{letter}' if list(hidden_word)[n] == letter else f'{Fore.YELLOW}{letter}' if letter in hidden_word else f'{Fore.WHITE}{letter}', end='')
                if list(hidden_word)[n] == letter: categorized_symbols["correct"].append(letter)
                if letter in hidden_word: categorized_symbols["another_place"].append(letter)
                if letter not in hidden_word: categorized_symbols["not_contain"].append(letter)
                
            print(f'{Style.RESET_ALL}')
        self.print_keyboard(symbols, categorized_symbols)

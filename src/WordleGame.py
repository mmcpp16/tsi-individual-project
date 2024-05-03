import random
from src.NormalModeComparer import NormalModeComparer
from src.HardModeComparer import HardModeComparer
from PyDictionary import PyDictionary

class WordleGame:
    WORD_LENGTH = 5
    MAX_GUESSES = 6

    def __init__(self, filename, comparer):
        self.filename = filename
        self.load_wordbank()
        self.reset_game()
        self.comparer = comparer
        self.dictionary = PyDictionary()

    def load_wordbank(self):
        try:
            with open(self.filename, 'r') as file:
                self.wordbank = file.read().split()
        except FileNotFoundError:
            print(f"Error: File '{self.filename}' not found.")

    def display_intro(self):
        print("\nWelcome to Wordle!\n")
        print("~~~" * 10)
        self.player_name = input("What is your name?: ")
        print("~~~" * 10)
        print(f"\n{self.player_name}, choose your game mode:\n1. Normal Mode\n2. Hard Mode")

        mode_choice = input("Enter your choice (1 or 2): ")
        if mode_choice == "1":
            self.comparer = NormalModeComparer()
            self.mode_description = "Normal Mode:\n If a letter is in the correct place, it will print in the word.\n If a letter is in the word but in the wrong place, it will print *.\n If a letter is not in the word, it will print -."
        elif mode_choice == "2":
            self.comparer = HardModeComparer()
            self.mode_description = "Hard Mode:\n You will only be told the number of correct or misplaced letters in your guess, not their locations."
        else:
            print("Invalid choice. Defaulting to Normal Mode.")
            self.comparer = NormalModeComparer()
            self.mode_description = "Normal Mode: If a letter is in the correct place, it will print in the word. If a letter is in the word but in the wrong place, it will print *. If a letter is not in the word, it will print -."

        print(f"\n{self.player_name}, you have {self.MAX_GUESSES} tries to guess the randomly selected {self.WORD_LENGTH}-letter word.")
        print("The word does not have any repeated characters.")
        print(f"\n{self.mode_description}")
        print("\nGood luck!")
        
    def reset_game(self):
        self.previous_guesses = set()
        self.word = random.choice(self.wordbank)
        self.guess_attempt = 0


    def is_valid_word(self, word):
        """Check if a word is a valid English word."""
        try:
            return self.dictionary.meaning(word, disable_errors=True) is not None
        except Exception as e:
            return False


    def get_user_guess(self):
        """Prompt user for a guess and validate it."""
        while True:
            guess = input(f"\nGuess attempt {self.guess_attempt + 1}: ").strip().upper()
            if len(guess) != self.WORD_LENGTH:
                print(f"Your guess must be a {self.WORD_LENGTH}-letter word. Try again!")
                continue
            if guess in self.previous_guesses:
                print("You've already guessed that word. Try a different one!")
                continue
            if not self.is_valid_word(guess):
                print("Not a valid input word. Try again!")
                continue
            return guess


    def play_game(self):
        self.display_intro()
        while self.guess_attempt < self.MAX_GUESSES:
            guess = self.get_user_guess()
            self.previous_guesses.add(guess)
            if guess == self.word:
                print("~~~" * 10)
                print(f"You win {self.player_name}! The word was {self.word}\nIt took you {self.guess_attempt + 1} guesses.")
                break
            else:
                self.guess_attempt += 1
                self.comparer.compare_words(self.word, guess)
        else:
            print("~~~" * 10)
            print(f"Unlucky {self.player_name}! The word was {self.word}")
        
        self.play_again()

    def play_again(self):
        choice = input("Do you want to play again? (yes/no): ").lower()
        if choice == 'yes':
            self.reset_game()
            self.play_game()
        else:
            print("Thank you for playing Wordle!")


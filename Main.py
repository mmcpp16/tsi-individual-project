from WordleGame import WordleGame
from WordComparer import WordComparer

if __name__ == "__main__":
    game = WordleGame('wordbank.txt', WordComparer())
    game.play_game()
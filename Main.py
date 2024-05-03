from src.WordleGame import WordleGame
from src.WordComparer import WordComparer

if __name__ == "__main__":
    game = WordleGame('wordbank.txt', WordComparer())
    game.play_game()

import sys
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from WordleGame import WordleGame
from LoadWordbankStub import load_wordbank

class TestWordleGameCommonMethods(unittest.TestCase):
        
    def test_load_wordbank(self):
        game = WordleGame('test_wordbank.txt', None)
        self.assertEqual(game.wordbank, ['ARISE', 'STARE', 'CANOE', 'SAUCE'])

    @patch('builtins.print')
    def test_file_not_found_error_handling(self, mock_print):
        with self.assertRaises(SystemExit):
            game = WordleGame('fake_file.txt', MagicMock())

    def test_reset_game_zeros_guesses(self):
        self.WordleGame = WordleGame('test_wordbank.txt', MagicMock())
        self.WordleGame.reset_game()
        self.assertEqual(self.WordleGame.guess_attempt, 0)

    def test_reset_game_clears_previous_guesses(self):
        self.WordleGame = WordleGame('test_wordbank.txt', MagicMock())
        self.WordleGame.reset_game()
        self.assertEqual(self.WordleGame.previous_guesses, set())
    
    
    def test_reset_game_selects_word_in_wordbank(self):
        self.WordleGame = WordleGame('test_wordbank.txt', MagicMock())
        self.WordleGame.reset_game()
        self.assertIn(self.WordleGame.word, self.WordleGame.wordbank)

    
if __name__ == '__main__':
    unittest.main()


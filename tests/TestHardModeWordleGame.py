import sys
import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from WordleGame import WordleGame
from LoadWordbankStub import load_wordbank

class TestNormalModeWordleGame(unittest.TestCase):
    @patch('builtins.input', side_effect=["Derek", "2"])  
    def test_display_hard_mode_intro(self, mock_input):
        game = WordleGame('test_wordbank.txt', None)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            game.display_intro()
            hard_mode_intro_message = fake_out.getvalue().strip()
        
        expected_hard_mode_intro_message = (
            'Welcome to Wordle!\n' 
            '\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
            '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'
            '\n'
            'Derek, choose your game mode:\n'
            '1. Normal Mode\n'
            '2. Hard Mode\n'
            '\n'
            'Derek, you have 6 tries to guess the randomly selected 5-letter word.\n'
            'The word does not have any repeated characters.\n'
            '\n'
            'Hard Mode:\n'
            ' You will only be told the number of correct or misplaced letters in your guess, not their locations.\n'
            '\n'
            'Good luck!'
        )
        self.assertEqual(hard_mode_intro_message, expected_hard_mode_intro_message)

    @patch('builtins.input', side_effect=['Derek', "2", 'ARISE', 'no'])
    def test_win_hard_mode_on_first_guess(self, mock_input):
        with patch('random.choice', return_value='ARISE') as mock_choice:
            with patch('builtins.print') as mock_print:
                game = WordleGame('test_wordbank.txt', MagicMock())
                game.play_game()
                mock_choice.assert_called_once_with(game.wordbank)
                mock_print.assert_any_call("You win Derek! The word was ARISE\nIt took you 1 guesses.")
                mock_print.assert_called_with('Thank you for playing Wordle!')

    @patch('builtins.input', side_effect=['Derek',"2", 'WORD', 'ARISE', 'no'])
    def test_hard_mode_get_user_guess_wrong_length(self, mock_input):
        with patch('random.choice', return_value='ARISE') as mock_choice:
            with patch('builtins.print') as mock_print:
                game = WordleGame('test_wordbank.txt', MagicMock())
                game.play_game()
                mock_print.assert_any_call("Your guess must be a 5-letter word. Try again!")
    
    @patch('builtins.input', side_effect=['Derek', "2", 'GHOUL', 'GHOUL', 'ARISE', 'no'])
    def test_hard_mode_get_user_guess_already_guessed(self, mock_input):
        with patch('random.choice', return_value='ARISE') as mock_choice:
            with patch('builtins.print') as mock_print:
                game = WordleGame('test_wordbank.txt', MagicMock())
                game.play_game()
                mock_print.assert_any_call("You've already guessed that word. Try a different one!")
    
    @patch('builtins.input', side_effect=['Derek', "1", 'QWERT', 'ARISE', 'no'])
    def test_hard_mode_get_user_guess_invalid_guess(self, mock_input):
        with patch('random.choice', return_value='ARISE') as mock_choice:
            with patch('builtins.print') as mock_print:
                game = WordleGame('test_wordbank.txt', MagicMock())
                game.play_game()
                mock_print.assert_any_call("Not a valid input word. Try again!")

    @patch('builtins.input', side_effect=['Derek', "2", 'MANGO', 'ARISE', 'no'])
    def test_hard_mode_win_not_on_first_guess(self, mock_input):
        with patch('random.choice', return_value='ARISE') as mock_choice:
            with patch('builtins.print') as mock_print:
                game = WordleGame('test_wordbank.txt', MagicMock())
                game.play_game()
                mock_choice.assert_called_once_with(game.wordbank)
                mock_print.assert_any_call("You win Derek! The word was ARISE\nIt took you 2 guesses.")
                mock_print.assert_called_with('Thank you for playing Wordle!')
    
    @patch('builtins.input', side_effect=['Derek', '1', 'MANGO', 'CANOE', 'GHOUL', 'LEMON', 'DRIFT', 'WHILE', 'no'])
    def test_hard_mode_max_guesses_reached(self, mock_input):
        with patch('random.choice', return_value='ARISE'):
            with patch('builtins.print') as mock_print:
                game = WordleGame('test_wordbank.txt', MagicMock())
                game.play_game()
                mock_print.assert_any_call("Unlucky Derek! The word was ARISE")
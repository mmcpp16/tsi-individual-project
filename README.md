# TSI Individual Project

## Project Introduction

My individual project is a command-line version of the game Wordle. It challenges players to guess a randomly selected 5-letter word within a limited number of attempts. The 'correct' word is selected from an .txt file with over 350 words.

The user can select 'normal' or 'hard' mode. This will determine the level of feedback they are given after each guess. The player can play multiple rounds, with the option to restart after each game.

Input validation ensures that user inputs guesses that are exactly 5 letters, and rejects duplicate guesses. The PyDictionary library is used to check that the user's guess is a valid word in the English dictionary. The user is prompted to guess again until valid input is provided. Additionally, error handling is implemented to address situations such as file not found errors when loading the word bank, ensuring a smooth user experience and robust functionality.

Tests are found in the subdirectory 'tests', and the program itself is run through the Main.py script.


## Doubling Tests

### Code to be Doubled

#### Class: WordleGame

Functions to be Doubled:

- load_wordbank: This function loads the word bank from a file. It involves file I/O, making it suitable for stubbing. It's stub can be found here.
- display_intro: This function takes user input for their name, and desired game mode. These inputs make it suitable for mocking.
- get_user_guess: This function takes user input for their guess, making it suitable for mocking.
- is_valid_word: This function checks if a word is valid by making an external call to an external dictionary API (via PyDictionary). It involves an external dependency, making it suitable for mocking.
- play_again: This function takes user input to ask if they'd like to play again, making it suitable for mocking.

#### Classes: HardModeComparer and NormalModeComparer

- compare_words (in HardModeComparer and NormalModeComparer): Each of these classes are concrete implementations of the abstract class WordComparer. They have respective feedback styles related to the difficulty of the mode. compare_words takes two inputs: the correct answer and the user's guess. Stubs are used to test these classes, as it allows the hardcoding of the inputs. This isolates the compare_words method, and reduces dependencies.

### Classes with Unit Tests

- TestWordleGameCommonMethods
- TestNormalModeWordleGame
- TestHardModeWordleGame
- TestNormalModeComparer
- TestHardModeComparer

#### Stubs

- LoadWordbankStub: This stub replaces the real implementation of loading the word bank with a predefined set of words. It allows isolating the test from external dependencies, ensuring consistent behaviour and predictable results during testing.
- test_load_wordbank: The test_load_wordbank method verifies that the stub is working correctly by checking if it returns the expected word bank.

#### Mocks

- test_invalid_word_handling - This test mocks the external dictionary call (PyDictionary.meaning) to simulate valid and invalid word checks.
- test_hard_mode_get_user_guess_invalid_guess: This method (along with all methods in TestNormalModeWordleGame and TestHardModeWordleGame) uses MagicMock to mock the user input and the random selection of word. This enables testing of user interactions and output messages without requiring actual user input or displaying messages to the console. Furthermore, mocking random.choice allows controlling the selected word during testing.

#### Fakes

- test_compare_words_all_cases_covered in (TestHardModeComparer and TestNormalModeComparer)
- test_compare_words_none_correct in (TestHardModeComparer and TestNormalModeComparer)
- test_compare_words_all_correct in (TestHardModeComparer and TestNormalModeComparer)

The methods in each of these classes are fakes. They provide hardcoded feedback for word comparisons, and logic to simulate the behavior of the real comparers. They are simplified versions of the actual comparers, meaning the game's logic can be tested without relying on external dependencies.

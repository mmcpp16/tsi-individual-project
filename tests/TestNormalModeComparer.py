import unittest
from NormalModeComparer import NormalModeComparer

class TestNormalModeComparer(unittest.TestCase):

    def setUp(self):
        self.comparer = NormalModeComparer()

    def test_compare_words_all_correct(self):
        word = "solid"
        guess = "solid"
        expected_feedback = ['s', 'o', 'l', 'i', 'd']
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_some_correct_rest_wrong(self):
        word = "solid"
        guess = "solve"
        expected_feedback = ['s', 'o', 'l', '-', '-']
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_none_correct(self):
        word = "solid"
        guess = "trace"
        expected_feedback = ['-', '-', '-', '-', '-']
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_some_correct_some_misplaced(self):
        word = "arise"
        guess = "raise"
        expected_feedback = ['*', '*', 'i', 's', 'e']
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_all_cases_covered(self):
        word = "solid"
        guess = "spoil"
        expected_feedback = ['s', '-', '*', 'i', '*']
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

if __name__ == '__main__':
    unittest.main()

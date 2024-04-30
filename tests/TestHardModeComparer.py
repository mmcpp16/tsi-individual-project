import unittest
from HardModeComparer import HardModeComparer

class TestHardModeComparer(unittest.TestCase):

    def setUp(self):
        self.comparer = HardModeComparer()

    def test_compare_words_all_correct(self):
        word = "solid"
        guess = "solid"
        expected_feedback = (5,0)
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_some_correct_rest_wrong(self):
        word = "solid"
        guess = "solve"
        expected_feedback = (3,0)
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_none_correct(self):
        word = "solid"
        guess = "trace"
        expected_feedback = (0,0)
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_some_correct_some_misplaced(self):
        word = "arise"
        guess = "raise"
        expected_feedback = (3,2)
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

    def test_compare_words_all_cases_covered(self):
        word = "solid"
        guess = "spoil"
        expected_feedback = (2,2)
        feedback = self.comparer.compare_words(word, guess)
        self.assertEqual(feedback, expected_feedback)

if __name__ == '__main__':
    unittest.main()

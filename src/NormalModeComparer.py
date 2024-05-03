from src.WordComparer import WordComparer

class NormalModeComparer(WordComparer):
    def compare_words(self, word, guess):
        feedback_symbols = [''] * len(word)
        for i, (char1, char2) in enumerate(zip(word, guess)):
            if char1 == char2:
                feedback_symbols[i] = char1
            elif char2 in word:
                feedback_symbols[i] = '*'
            else:
                feedback_symbols[i] = '-'
        print("Feedback:", " ".join(feedback_symbols))
        return feedback_symbols

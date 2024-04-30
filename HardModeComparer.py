from WordComparer import WordComparer

class HardModeComparer(WordComparer):
    def compare_words(self, word, guess):
        correct_letters = 0
        misplaced_letters = 0
        for i, (char1, char2) in enumerate(zip(word, guess)):
            if char1 == char2:
                correct_letters +=1
            elif char2 in word:
                misplaced_letters +=1
        print("Correctly placed letters:", correct_letters,"\nMisplaced letters:", misplaced_letters)


from abc import abstractmethod

class WordComparer():
    @abstractmethod
    def compare_words(self, word, guess):
        pass
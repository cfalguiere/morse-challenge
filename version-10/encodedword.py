class EncodedWord():

    def __init__(self, word, duplicates=1):
        self.word = word
        self.duplicates = duplicates

    def add_duplicate(self):
        self.duplicates += 1

    def __repr__(self):
        return f'{self.word}#{self.duplicates}' if self.duplicates > 1 else self.word

    def __len__(self):
        return len(self.word)

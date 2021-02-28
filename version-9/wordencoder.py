from alphabet import MorseAlphabet


class WordEncoder():
    def __init__(self, sep='', alphabet=None):
        self.encoded_dict = {}
        self.sep = sep
        if alphabet:
            self.alphabet = alphabet
        else:
            self.alphabet = MorseAlphabet()

    def get_alphabet(self):
        return self.alphabet

    def get_list(self):
        return list(self.encoded_dict.keys())

    def get_dict(self):
        return self.encoded_dict

    def add_word_list(self, words):
        [self.add_word(w) for w in words]

    def add_word(self, word):
        alphabet_map = self.alphabet.get_encoded_letters_map()
        letters = []
        for letter in word:
            letters.append(alphabet_map[letter])
        encoded_word = self.sep.join(letters)
        if encoded_word in self.encoded_dict:
            self.encoded_dict[encoded_word] += 1
        else:
            self.encoded_dict[encoded_word] = 1

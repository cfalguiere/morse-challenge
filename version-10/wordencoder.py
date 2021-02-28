from encodedword import EncodedWord


class WordEncoder():
    def __init__(self, context, sep='', use_size_index=False, use_screening=False):
        self.encoded_dict = {}
        self.index_dict = {}
        self.sep = sep  # sep between letters in encoded key
        self.alphabet = context.get_alphabet()
        self.sentence = context.get_sentence()
        self.context = context
        self.use_size_index = use_size_index
        self.use_screening = use_screening

    def __len__(self):
        return len(self.encoded_dict.keys())

    def get_list(self):
        return list(self.encoded_dict.keys())

    def get_dict(self):
        return self.encoded_dict

    def get_index_dict(self):
        return self.index_dict

    def add_word_list(self, words):
        [self.add_word(w) for w in words]

    def add_word(self, word_str):
        encoded_word = self.alphabet.encode_word(word_str, sep=self.sep)

        if self.use_screening:
            if self.sentence.find(encoded_word) < 0:
                return

        word = None
        if encoded_word in self.encoded_dict:
            word = self.encoded_dict[encoded_word]
            word.add_duplicate()
        else:
            word = EncodedWord(encoded_word)
            self.encoded_dict[encoded_word] = word

        if self.use_size_index:
            key = len(encoded_word)
            if key not in self.index_dict:
                self.index_dict[key] = []
            self.index_dict[key].append(word)

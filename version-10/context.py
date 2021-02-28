class Context():
    def __init__(self):
        self.data = {}

    def add_sentence(self, sentence):
        self.data['sentence'] = sentence

    def get_sentence(self):
        return self.data['sentence']

    def add_alphabet(self, alphabet):
        self.data['alphabet'] = alphabet

    def get_alphabet(self):
        return self.data['alphabet']

    def add_word_encoder(self, encoder):
        self.data['word_encoder'] = encoder

    def get_word_encoder(self):
        return self.data['word_encoder']

    def add_word_finder(self, finder):
        self.data['word_finder'] = finder

    def get_word_finder(self):
        return self.data['word_finder']

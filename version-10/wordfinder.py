class WordFinder:
    def __init__(self, context):
        self.context = context
        self.sentence = context.get_sentence()
        self.word_dict = context.get_word_encoder().get_dict()

    def find_slice(self, pos, length):
        options = []
        for key, encoded_word in self.word_dict.items():
            nb_word_signs = len(key)
            if nb_word_signs <= length:
                if self.sentence.find(key, pos) == pos:
                    options.append(encoded_word)
        return options

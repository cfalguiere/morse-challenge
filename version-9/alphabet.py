class MorseAlphabet():

    def __init__(self):
        self.letters = '''A  .- 	 B  -... 	 C  -.-. 	 D  -..
        E  . 	 F  ..-. 	 G  --. 	 H  ....
        I  .. 	 J  .--- 	 K  -.- 	 L  .-..
        M  -- 	 N  -. 	 O  --- 	 P  .--.
        Q  --.- 	 R  .-. 	 S  ... 	 T  -
        U  ..- 	 V  ...- 	 W  .-- 	 X  -..-
        Y  -.-- 	 Z  --..'''
        self.encoded_letters_map = self.__generate_alphabet_map()
        self.encoded_letters = list(self.encoded_letters_map.values())

    def get_encoded_letters(self):
        return self.encoded_letters

    def get_encoded_letters_map(self):
        return self.encoded_letters_map

    def encode(self, letter):
        return self.encoded_letters_map[letter]

    def __generate_alphabet_map(self):
        key = None
        alphabet_map = {}
        for value in self.letters.split():
            if key is not None:
                alphabet_map[key] = value
                key = None
            else:
                key = value
        return alphabet_map

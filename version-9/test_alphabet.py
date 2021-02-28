from alphabet import MorseAlphabet


def test_encode():
    morse = MorseAlphabet()
    assert morse.encode('D') == '-..'


def test_encoded_letters_first_line():
    morse = MorseAlphabet()
    assert '-..' in morse.get_encoded_letters()
    assert morse.get_encoded_letters_map()['D'] == '-..'


def test_encoded_letters_second_line():
    morse = MorseAlphabet()
    assert morse.encode('I') == '..'
    assert '.---' in morse.get_encoded_letters()
    assert morse.get_encoded_letters_map()['I'] == '..'


def test_encoded_letters_ident_second_line():
    morse = MorseAlphabet()
    assert morse.encode('J') == '.---'
    assert '.---' in morse.get_encoded_letters()
    assert morse.get_encoded_letters_map()['J'] == '.---'

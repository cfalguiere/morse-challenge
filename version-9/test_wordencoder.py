from alphabet import MorseAlphabet
from wordencoder import WordEncoder


def test_add_one_word():
    encoder = WordEncoder()

    encoder.add_word('HTE')
    encoded_dict = encoder.get_dict()
    assert encoded_dict['....-.'] == 1
    encoder.add_word('HTE')
    encoded_dict = encoder.get_dict()
    assert encoded_dict['....-.'] == 2
    assert len(encoder.get_list()) == 1


def test_add_one_word_with_alphabet():
    morse = MorseAlphabet()
    encoder = WordEncoder(sep='|', alphabet=morse)
    encoder.add_word('HTE')
    encoded_dict = encoder.get_dict()
    assert encoded_dict['....|-|.'] == 1


def test_add_word_list():
    encoder = WordEncoder()
    encoder.add_word_list(['HTE', 'EE'])
    encoded_dict = encoder.get_dict()
    assert encoded_dict['....-.'] == 1
    assert encoded_dict['..'] == 1
    assert len(encoder.get_list()) == 2

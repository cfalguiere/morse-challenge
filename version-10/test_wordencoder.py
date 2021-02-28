import pytest

from alphabet import MorseAlphabet
from context import Context
from wordencoder import WordEncoder


@pytest.fixture
def context():
    context = Context()
    context.add_sentence('......-...-..---')  # HELLO
    context.add_alphabet(MorseAlphabet())
    return context


def test_add_one_word(context):
    encoder = WordEncoder(context)
    encoded_dict = encoder.get_dict()

    encoder.add_word('HTE')
    word = encoded_dict['....-.']
    assert word.duplicates == 1
    assert word.word == '....-.'
    assert len(encoder) == 1


def test_add_two_words(context):
    encoder = WordEncoder(context)
    encoded_dict = encoder.get_dict()

    encoder.add_word('HTE')
    assert str(encoded_dict['....-.']) == '....-.'

    encoder.add_word('ET')
    assert str(encoded_dict['.-']) == '.-'

    assert len(encoder) == 2


def test_add_two_word_with_duplicates(context):
    encoder = WordEncoder(context)
    encoded_dict = encoder.get_dict()

    encoder.add_word('HTE')
    assert str(encoded_dict['....-.']) == '....-.'

    encoder.add_word('HTE')
    assert str(encoded_dict['....-.']) == '....-.#2'

    assert len(encoder) == 1


def test_add_two_word_with_screening(context):
    encoder = WordEncoder(context, use_screening=True)
    encoded_dict = encoder.get_dict()

    encoder.add_word('HTE')
    assert str(encoded_dict['....-.']) == '....-.'

    encoder.add_word('K')
    assert '-.-' not in encoded_dict

    assert len(encoder) == 1


def test_add_two_word_indexed(context):
    encoder = WordEncoder(context, use_size_index=True)
    index = encoder.get_index_dict()

    encoder.add_word('ET')
    assert index[2][0].word == '.-'
    encoder.add_word('EE')
    assert index[2][1].word == '..'
    encoder.add_word('EM')
    assert index[3][0].word == '.--'


def test_add_one_word_with_sep(context):
    encoder = WordEncoder(context, sep='|')
    encoded_dict = encoder.get_dict()
    encoder.add_word('HTE')
    assert encoded_dict['....|-|.'].word == '....|-|.'


def test_add_word_list(context):
    encoder = WordEncoder(context)
    encoded_dict = encoder.get_dict()
    encoder.add_word_list(['HTE', 'EE'])
    assert encoded_dict['....-.'].word == '....-.'
    assert encoded_dict['..'].word == '..'
    assert len(encoder.get_list()) == 2

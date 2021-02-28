import pytest

from alphabet import MorseAlphabet
from context import Context
from wordencoder import WordEncoder
from wordfinder import WordFinder


@pytest.fixture
def context1():
    context = Context()
    context.add_sentence('......-...-..---')  # HELLO
    context.add_alphabet(MorseAlphabet())

    encoder = WordEncoder(context)
    context.add_word_encoder(encoder)
    encoder.add_word('HELLO')
    encoder.add_word('HELL')
    encoder.add_word('TEST')
    return context


@pytest.fixture
def context2():
    context = Context()
    context.add_sentence('--')  # TT M
    context.add_alphabet(MorseAlphabet())

    encoder = WordEncoder(context)
    context.add_word_encoder(encoder)
    encoder.add_word('T')
    return context


def test_find_word(context1):
    finder = WordFinder(context1)

    options = finder.find_slice(0, 16)
    assert options
    assert len(options) == 2
    assert options[0].word == '......-...-..---'
    assert options[1].word == '......-...-..'


def test_find_word_2(context2):
    finder = WordFinder(context2)

    options = finder.find_slice(0, 2)
    assert len(options) == 1
    assert options[0].word == '-'

    options = finder.find_slice(1, 1)
    assert len(options) == 1
    assert options[0].word == '-'

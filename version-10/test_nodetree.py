import pytest

from alphabet import MorseAlphabet
from context import Context
from wordencoder import WordEncoder
from wordfinder import WordFinder

from node import NodeState
from nodetree import NodeTree


@pytest.fixture
def context1():
    context = Context()
    context.add_sentence('......-...-..---')  # HELLO
    context.add_alphabet(MorseAlphabet())

    encoder = WordEncoder(context)
    context.add_word_encoder(encoder)
    encoder.add_word('HELLO')

    context.add_word_finder(WordFinder(context))

    return context


@pytest.fixture
def context2():
    context = Context()
    context.add_sentence('......-...-..---')  # HELLO
    context.add_alphabet(MorseAlphabet())

    encoder = WordEncoder(context)
    context.add_word_encoder(encoder)
    encoder.add_word('HELL')
    encoder.add_word('O')  # invalid in pos 0

    context.add_word_finder(WordFinder(context))

    return context


@pytest.fixture
def context3():
    context = Context()
    context.add_sentence('......-...-..---')  # HELLO
    context.add_alphabet(MorseAlphabet())

    encoder = WordEncoder(context)
    context.add_word_encoder(encoder)
    encoder.add_word('HELLO')
    encoder.add_word('HELL')
    encoder.add_word('O')  # invalid in pos 0

    context.add_word_finder(WordFinder(context))

    return context


@pytest.fixture
def context4():
    context = Context()
    context.add_sentence('......-...-..---')  # HELLO
    context.add_alphabet(MorseAlphabet())

    encoder = WordEncoder(context)
    context.add_word_encoder(encoder)
    encoder.add_word('HELLO')
    encoder.add_word('EEEEELLO')  # same encoding

    context.add_word_finder(WordFinder(context))

    return context


def test_root_node(context1):
    tree = NodeTree(context1)
    next_node = tree.root
    assert next_node.state == NodeState.ROOT
    assert next_node.pos == 0
    assert next_node.nb_remaining == len(context1.get_sentence())
    assert len(next_node.options) == 1  # HELLO


def test_single_match_in_one_step(context1):
    tree = NodeTree(context1)
    node = tree.next()
    assert node.state == NodeState.CHILD
    assert node.segment.word == '......-...-..---'
    assert node.pos == 0
    len_sentence = len(context1.get_sentence())
    len_before = node.pos
    len_word = len(node.segment)
    len_remaining = node.nb_remaining
    assert len_before + len_word + len_remaining == len_sentence
    assert len(node.options) == 0  # no more options
    assert node.is_done

    assert tree.next() is None


def test_one_match_in_two_steps(context2):
    tree = NodeTree(context2)
    len_sentence = len(context2.get_sentence())

    node1 = tree.next()
    assert node1.state == NodeState.CHILD
    assert node1.segment.word == '......-...-..'
    assert node1.pos == 0
    len_before = node1.pos
    len_word = len(node1.segment)
    len_remaining = node1.nb_remaining
    assert len_before + len_word + len_remaining == len_sentence
    assert len(node1.options) == 1  # O
    assert node1.is_done is False

    node2 = tree.next()
    assert node2.state == NodeState.CHILD
    assert node2.segment.word == '---'
    assert node2.pos == 13
    len_before = node2.pos
    len_word = len(node2.segment)
    len_remaining = node2.nb_remaining
    assert len_before + len_word + len_remaining == len_sentence
    assert len(node2.options) == 0  # no more options
    assert node2.is_done

    assert tree.next() is None

def test_two_match_three_step(context3):
    tree = NodeTree(context3)
    len_sentence = len(context3.get_sentence())

    node1 = tree.next()
    assert node1.state == NodeState.CHILD
    assert node1.segment.word == '......-...-..'
    assert node1.pos == 0
    len_before = node1.pos
    len_word = len(node1.segment)
    len_remaining = node1.nb_remaining
    assert len_before + len_word + len_remaining == len_sentence
    assert len(node1.options) == 1  # O
    assert node1.is_done is False

    node2 = tree.next()
    assert node2.state == NodeState.CHILD
    assert node2.segment.word == '---'
    assert node2.pos == 13
    len_before = node2.pos
    len_word = len(node2.segment)
    len_remaining = node2.nb_remaining
    assert len_before + len_word + len_remaining == len_sentence
    assert len(node2.options) == 0  # no more options
    assert node2.is_done is True

    node3 = tree.next()
    assert node3.state == NodeState.CHILD
    assert node3.segment.word == '......-...-..---'
    assert node3.pos == 0
    len_before = node3.pos
    len_word = len(node3.segment)
    len_remaining = node3.nb_remaining
    assert len_before + len_word + len_remaining == len_sentence
    assert len(node3.options) == 0  # no more options
    assert node3.is_done

    assert tree.next() is None


def test_one_match_with_duplicates(context4):
    tree = NodeTree(context4)

    current_node = tree.next()
    while current_node:
        assert current_node.total_options == 2
        current_node = tree.next()

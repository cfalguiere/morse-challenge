import pytest

from node import NodeState, Node


@pytest.fixture
def sentence1():
    sentence = '..-.--.'
    return sentence


@pytest.fixture
def sentence2():
    sentence = '..--'
    return sentence


def test_root_node(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    assert node_0.state == NodeState.ROOT
    # assert node_0.remaining == sentence1
    assert node_0.nb_remaining == len(sentence1)


def test_child_node(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    assert node_1.state == NodeState.CHILD
    assert node_1.segment == '..'
    assert node_1.pos == 0
    assert node_1.next_pos == 2
    #assert node_1.remaining == '-.--.'
    assert node_1.nb_remaining == len('-.--.')
    assert node_1.parent == node_0


def test_next_pos(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    assert node_1.next_pos == 2
    node_2 = Node('-', 2, len('.--.'), parent=node_1)
    assert node_2.next_pos == 3


def test_next_done_ongoing(sentence2):
    # node_0 = Node('', 0, sentence2, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence2), state=NodeState.ROOT)
    node_1 = Node('..', 2, len('--'), parent=node_0)
    assert node_1.is_done is False


def test_next_done_completed(sentence2):
    # node_0 = Node('', 0, sentence2, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence2), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('--'), parent=node_0)
    node_2 = Node('--', 2, len(''), parent=node_1)
    assert node_2.is_done is True


def test_find_origin(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    node_2 = Node('-', 2, len('.--.'), parent=node_1)
    node_3 = Node('.--', 5, len('.'), parent=node_2)
    node_4 = Node('.', 6, len(''), parent=node_3)
    origin = node_4.get_sequence_start()
    assert origin.get_sequence() == ''
    assert origin.state == NodeState.ROOT


def test_one_item_sequence(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    print(node_1.get_sequence())
    assert node_1.get_sequence() == '..'
    assert node_1.get_sum_length_sequence() == 2


def test_many_items_sequence(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    node_2 = Node('-', 2, len('.--.'), parent=node_1)
    node_3 = Node('.--', 5, len('.'), parent=node_2)
    assert node_2.get_sequence() == '..|-'
    assert node_2.get_sum_length_sequence() == 3
    assert node_3.get_sequence() == '..|-|.--'
    assert node_3.get_sum_length_sequence() == 6


def test_nb_options(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    node_2 = Node('-', 2, len('.--.'), parent=node_1)
    node_3 = Node('.--', 5, len('.'), parent=node_2)
    node_4 = Node('.', 6, len(''), parent=node_3)
    assert node_4.get_nb_options() == 1


def test_nb_options_with_duplicates(sentence1):
    # node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    node_0 = Node('', 0, len(sentence1), state=NodeState.ROOT)
    node_1 = Node('..', 0, len('-.--.'), parent=node_0)
    node_2 = Node('-', 2, len('.--.'), parent=node_1, duplicates=3)
    node_3 = Node('.--', 5, len('.'), parent=node_2)
    node_4 = Node('.', 6, len(''), parent=node_3, duplicates=2)
    assert node_4.get_nb_options() == 6

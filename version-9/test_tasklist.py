import pytest


from node import NodeState, Node


from tasklist import TaskList


@pytest.fixture
def sentence1():
    sentence = '..-.--.'
    return sentence


def test_first_task(sentence1):
    node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    tasklist = TaskList(node_0)
    next_node = tasklist.next()
    assert next_node.remaining == sentence1


def test_task_order(sentence1):
    node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    tasklist = TaskList(node_0)

    node_1a = Node('6', 6, '', parent=node_0)
    tasklist.add(node_1a)
    node_1b = Node('5', 5, '', parent=node_0)
    tasklist.add(node_1b)
    node_1c = Node('2', 2, '', parent=node_0)
    tasklist.add(node_1c)
    node_1d = Node('3', 3, '', parent=node_0)
    tasklist.add(node_1d)
    node_1e = Node('4', 4, '', parent=node_0)
    tasklist.add(node_1e)
    node_1f = Node('1', 1, '', parent=node_0)
    tasklist.add(node_1f)

    assert len(tasklist) == 7

    next_node = tasklist.next()
    assert next_node.next_pos == 7
    assert len(tasklist) == 6

    next_node = tasklist.next()
    assert next_node.next_pos == 6
    assert len(tasklist) == 5


def test_simple_path(sentence1):
    node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    tasklist = TaskList(node_0)
    assert len(tasklist) == 1

    next_node_0 = tasklist.next()
    assert len(tasklist) == 0
    assert next_node_0.next_pos == 0

    node_1 = Node('..', 0, '-.--.', parent=next_node_0)
    tasklist.add(node_1)
    next_node_1 = tasklist.next()
    assert len(tasklist) == 0
    assert next_node_1.next_pos == 2

    node_2 = Node('-', 2, '.--.', parent=next_node_1)
    tasklist.add(node_2)
    next_node_2 = tasklist.next()
    assert len(tasklist) == 0
    assert next_node_2.next_pos == 3

    node_3 = Node('.--', 3, '.', parent=next_node_2)
    tasklist.add(node_3)
    next_node_3 = tasklist.next()
    assert len(tasklist) == 0
    assert next_node_3.next_pos == 6

    node_4 = Node('.', 6, '', parent=next_node_3)
    tasklist.add(node_4)
    next_node_4 = tasklist.next()
    assert len(tasklist) == 0
    assert next_node_4.next_pos == 7

    next_node_done = tasklist.next()
    assert next_node_done is None


def test_take_2(sentence1):
    node_0 = Node('', 0, sentence1, state=NodeState.ROOT)
    tasklist = TaskList(node_0)
    assert len(tasklist) == 1

    nodes = tasklist.next(size=2)
    assert len(nodes) == 1
    next_node_0 = nodes[0]
    assert len(tasklist) == 0
    assert next_node_0.next_pos == 0

    node_1 = Node('..', 0, '-.--.', parent=next_node_0)
    tasklist.add(node_1)
    node_2 = Node('-', 2, '.--.', parent=node_1)
    tasklist.add(node_2)

    nodes = tasklist.next(size=2)
    assert len(nodes) == 2

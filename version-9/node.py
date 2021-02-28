from enum import Enum


class NodeState(Enum):
    ROOT = 1
    CHILD = 2
    TERMINAL = 3


class Node():

    def __init__(self,
                 segment, pos,
                 #remaining,
                 nb_remaining,
                 level=0,
                 duplicates=1,
                 parent=None,
                 state=NodeState.CHILD):

        self.state = state

        self.parent = parent

        self.segment = segment
        self.duplicates = duplicates

        self.pos = pos
        self.length = len(segment)
        self.next_pos = pos + self.length

        self.level = level

        #self.remaining = remaining
        #self.is_done = True if not remaining else False
        self.nb_remaining = nb_remaining
        self.is_done = False if nb_remaining > 0 else True

    def __repr__(self):
        text = '<Node>%s' % self.segment
        return text

    def get_sequence(self, sep='|'):
        sequence = []
        current = self
        while current.state == NodeState.CHILD:
            sequence.append(current.segment)
            current = current.parent
        sequence.reverse()
        text = sep.join(sequence)
        return text

    def get_length_sequence(self):
        sequence = []
        current = self
        while current.state == NodeState.CHILD:
            sequence.append(current.length)
            current = current.parent
        sequence.reverse()
        return sequence

    def get_sum_length_sequence(self):
        return sum(self.get_length_sequence())

    def get_nb_options(self):
        nb_options = 1
        current = self
        while current.state == NodeState.CHILD:
            nb_options *= current.duplicates
            current = current.parent
        return nb_options

    def get_nb_options_from_root(self):
        nb_options = 1
        current = self
        while current.state == NodeState.CHILD:
            nb_options *= current.duplicates
            current = current.parent
        return nb_options

    def get_sequence_start(self):
        current = self
        while current.state == NodeState.CHILD:
            current = current.parent
        return current

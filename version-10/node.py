from enum import Enum


class NodeState(Enum):
    ROOT = 1
    CHILD = 2
    TERMINAL = 3


class Node():

    def __init__(self,
                 segment,
                 parent=None,
                 target_length=None,
                 state=NodeState.CHILD):

        self.segment = segment
        self.parent = parent
        self.state = state

        self.children = []
        self.options = None

        if state == NodeState.CHILD:
            self.pos = parent.next_pos
            self.length = len(segment)
            self.next_pos = self.pos + self.length

            # self.remaining = remaining
            # self.is_done = True if not remaining else False
            self.nb_remaining = parent.nb_remaining - self.length
            self.is_done = False if self.nb_remaining > 0 else True

            self.level = parent.level + 1
            self.total_options = parent.total_options * self.segment.duplicates
            parent.children.append(self)

        if state == NodeState.ROOT:
            self.pos = 0
            self.next_pos = self.pos
            self.nb_remaining = target_length
            self.level = 0
            self.total_options = 1
            self.is_done = False

    def __repr__(self):
        text = f'<Node>{self.segment} at pos:{self.pos} - rem:{self.nb_remaining} options:{self.options}'
        return text

    def add_options(self, options):
        self.options = options.copy()

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
        return self.total_options

    def get_nb_options_old(self):
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

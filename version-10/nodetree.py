from node import Node, NodeState


class NodeTree():

    def __init__(self, context):
        self.context = context
        self.sentence = context.get_sentence()
        self.word_finder = context.get_word_finder()

        # create root
        len_sentence = len(self.sentence)
        self.root = Node(None, target_length=len_sentence, state=NodeState.ROOT)
        options = self.word_finder.find_slice(0, len_sentence)
        self.root.add_options(options)
        self.current = self.root

    def new_node(self, current_node):
        option = current_node.options.pop()
        new_node = Node(option, parent=current_node)
        options = self.word_finder.find_slice(new_node.next_pos, new_node.nb_remaining)
        new_node.add_options(options)
        return new_node

    def next(self):
        current_node = self.current
        new_node = None
        while current_node and not new_node:
            if current_node.options:
                new_node = self.new_node(current_node)
            elif current_node.parent:
                current_node = current_node.parent
            else:
                current_node = None
                new_node = None

        self.current = new_node
        return self.current

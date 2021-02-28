from collections import deque


class TaskList():

    def __init__(self, root_node):
        self.node_buckets = {}
        self.node_buckets[root_node.next_pos] = [root_node]

    def __len__(self):
        return sum([len(v) for k, v in self.node_buckets.items()])

    def __repr__(self):
        text = f'<TaskList>{self.nodes}'
        return text

    def add(self, node):
        if node.next_pos in self.node_buckets.keys():
            self.node_buckets[node.next_pos].append(node)
        else:
            self.node_buckets[node.next_pos] = [node]

    def next(self, size=1):
        selected_nodes = []
        sorted_keys = sorted(self.node_buckets.keys(), reverse=True)
        while not selected_nodes and sorted_keys:
            bucket_key = sorted_keys[0]
            # print(f'bucket_key {bucket_key}')
            selected_nodes.extend(self.node_buckets[bucket_key])
            # print(f'nodes {nodes}')
            if selected_nodes:
                self.node_buckets[bucket_key] = []
            else:
                sorted_keys.pop(0)

        return selected_nodes

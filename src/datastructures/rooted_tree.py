class RootedTree:
    def __init__(self, root=None):
        self.root = root


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left_child = None
        self.right_sibling = None

import random

from datastructures import binary_tree


class Treap(binary_tree.BinaryTree):
    pass


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.priority = random.uniform(0, 1)

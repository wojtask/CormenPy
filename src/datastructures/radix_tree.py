from datastructures import binary_tree


class RadixTree(binary_tree.BinaryTree):
    pass


class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.in_tree = False

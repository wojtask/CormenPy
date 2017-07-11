from datastructures import binary_tree


class AVLTree(binary_tree.BinaryTree):
    pass


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.h = 0

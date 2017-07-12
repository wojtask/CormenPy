import math
from enum import Enum

from datastructures import binary_tree


class Color(Enum):
    RED = 0
    BLACK = 1


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.color = Color.BLACK


class RedBlackTree(binary_tree.BinaryTree):
    def __init__(self, root=None, nil=Node(None)):
        super().__init__(root)
        self.nil = nil
        self.nil.left = self.nil.right = self.nil.p = self.nil
        if root is None:
            self.root = self.nil
        else:
            self.root.p = self.nil
            self._assign_sentinel_to_empty_children(root)

    def _assign_sentinel_to_empty_children(self, node):
        if node.left is None:
            node.left = self.nil
        else:
            self._assign_sentinel_to_empty_children(node.left)
        if node.right is None:
            node.right = self.nil
        else:
            self._assign_sentinel_to_empty_children(node.right)


class OSNode(Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.size = 0


class IntervalNode(Node):
    def __init__(self, key, interval, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.int = interval
        self.max = -math.inf

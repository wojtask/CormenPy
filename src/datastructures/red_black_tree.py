from enum import Enum

from datastructures import binary_tree
from datastructures.binary_tree import BinaryTree


class Color(Enum):
    RED = 0
    BLACK = 1


class RedBlackTree(BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)
        self.nil = Node(None)
        if root is None:
            self.root = self.nil
        else:
            self.root.p = self.nil
            self._assign_sentinel_to_empty_children(root)

    def _assign_sentinel_to_empty_children(self, x):
        if x.left is None:
            x.left = self.nil
        else:
            self._assign_sentinel_to_empty_children(x.left)
        if x.right is None:
            x.right = self.nil
        else:
            self._assign_sentinel_to_empty_children(x.right)


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right)
        self.color = color

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key and self.data == other.data and \
                   self.left == other.left and self.right == other.right and self.color == other.color
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

from enum import Enum

from datastructures import binary_tree


class Color(Enum):
    RED = 0
    BLACK = 1


class RedBlackTree(binary_tree.BinaryTree):
    def __init__(self, root=None):
        super().__init__(root)
        self.nil = Node(None)
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


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right)
        self.color = color

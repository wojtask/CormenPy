import math

from datastructures import binary_tree

Red = 0
Black = 1


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None, color=Black):
        super().__init__(key, data, left, right)
        self.color = color


class RedBlackTree(binary_tree.BinaryTree):
    def __init__(self, root=None, sentinel=Node(None)):
        super().__init__(root)
        self.nil = sentinel
        if sentinel is not None:
            self.nil.left = self.nil.right = self.nil
        if root is None:
            self.root = self.nil
        else:
            self.root.p = self.nil
            if sentinel is not None:
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


class ParentlessNode(binary_tree.ParentlessNode):
    def __init__(self, key, data=None, left=None, right=None, color=Black):
        super().__init__(key, data, left, right)
        self.color = color

    @classmethod
    def clone(cls, node):
        return cls(node.key, node.data, node.left, node.right, node.color)


class OSNode(Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.size = 0


class IntervalNode(Node):
    def __init__(self, key, interval, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.int = interval
        self.max = -math.inf


class IntervalPomNode(Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.low = self.high = 0
        self.sum = 0
        self.max = -math.inf
        self.pom = None

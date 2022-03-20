import math
from enum import Enum, auto

from datastructures import binary_tree


class Color(Enum):
    RED = auto()
    BLACK = auto()


class Node(binary_tree.Node):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
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


class ParentlessNode(binary_tree.ParentlessNode):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right)
        self.color = color

    @classmethod
    def clone(cls, node):
        return cls(node.key, node.data, node.left, node.right, node.color)


class OSNode(Node):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right, color)
        self.size = 0


class AugmentedOSNode(OSNode):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.min = self
        self.max = self
        self.pred = self
        self.succ = self


class IntervalNode(Node):
    def __init__(self, key, interval=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, None, left, right, color)
        self.int = interval
        self.max = -math.inf


class MinGapNode(Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.min_key = math.inf
        self.max_key = -math.inf
        self.min_gap = math.inf


class IntervalPomNode(Node):
    def __init__(self, key, left=None, right=None):
        super().__init__(key, left, right)
        self.low = 0
        self.high = 0
        self.sum = 0
        self.max = -math.inf
        self.pom = None

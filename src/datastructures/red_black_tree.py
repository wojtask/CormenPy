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
        if sentinel is not None:
            self.nil = sentinel
            self.nil.left = self.nil.right = self.nil
            if hasattr(sentinel, 'p'):
                self.nil.p = self.nil
            if root is None:
                self.root = self.nil
            elif hasattr(root, 'p'):
                self.root.p = self.nil


class ParentlessNode(binary_tree.ParentlessNode):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right)
        self.color = color

    @classmethod
    def clone(cls, node):
        return cls(node.key, node.data, node.left, node.right, node.color)


class JoinableRedBlackTree(RedBlackTree):
    def __init__(self, root=None, bh=0):
        super().__init__(root=root, sentinel=None)
        self.bh = bh


class OSNode(Node):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right, color)
        self.size = 0


class RankedOSNode(Node):
    def __init__(self, key, data=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, data, left, right, color)
        self.rank = None


class ChainedOSNode(OSNode):
    def __init__(self, key):
        super().__init__(key)
        self.prev = self
        self.next = self


class IntervalNode(Node):
    def __init__(self, key, interval=None, left=None, right=None, color=Color.BLACK):
        super().__init__(key, None, left, right, color)
        self.int = interval
        self.max = -math.inf


class MinGapNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.min_key = math.inf
        self.max_key = -math.inf
        self.min_gap = math.inf


class IntervalPomNode(Node):
    def __init__(self, key):
        super().__init__(key)
        self.low = 0
        self.high = 0
        self.sum = 0
        self.max = -math.inf
        self.pom = None

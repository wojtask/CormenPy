import random

from datastructures.essential import Element
from datastructures.rooted_tree import RootedTree


class BinaryTree(RootedTree):
    pass


class Node(Element):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data)
        self.left = left
        if left is not None:
            left.p = self
        self.right = right
        if right is not None:
            right.p = self
        self.p = None


class ParentlessNode(Element):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data)
        self.left = left
        self.right = right


class RadixNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.in_tree = False


class AVLNode(ParentlessNode):
    def __init__(self, key):
        super().__init__(key)
        self.h = 0


class TreapNode(Node):
    def __init__(self, key, data=None, left=None, right=None):
        super().__init__(key, data, left, right)
        self.priority = random.uniform(0, 1)


class HuffmanNode(ParentlessNode):
    def __init__(self, character=None, frequency=0):
        super().__init__(frequency, character)
        self.f = frequency

    def __lt__(self, other):
        if isinstance(other, float):
            return self.f < other
        return self.f < other.f

    def __gt__(self, other):
        if isinstance(other, float):
            return self.f > other
        return self.f > other.f


class TernaryHuffmanNode(HuffmanNode):
    def __init__(self, character=None, frequency=0):
        super().__init__(character, frequency)
        self.middle = None


class NodeWithSize(Node):
    def __init__(self, key):
        super().__init__(key)
        self.size = 0

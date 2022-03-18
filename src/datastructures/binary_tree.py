from datastructures.rooted_tree import RootedTree
from util import Element


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

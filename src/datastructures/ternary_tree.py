from datastructures.rooted_tree import RootedTree


class TernaryTree(RootedTree):
    pass


class Node:
    def __init__(self, key, data=None, left=None, middle=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        if left is not None:
            left.p = self
        self.middle = middle
        if middle is not None:
            middle.p = self
        self.right = right
        if right is not None:
            right.p = self
        self.p = None

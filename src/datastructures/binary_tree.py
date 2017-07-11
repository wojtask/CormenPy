class BinaryTree:
    def __init__(self, root=None):
        self.root = root


class Node:
    def __init__(self, key, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        if left is not None:
            left.p = self
        self.right = right
        if right is not None:
            right.p = self
        self.p = None


class ParentlessNode:
    def __init__(self, key, data=None, left=None, right=None):
        self.key = key
        self.data = data
        self.left = left
        self.right = right

import math


class RootedTree:
    def __init__(self, root=None):
        self.root = root


class Node:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left_child = None
        self.right_sibling = None


class EmployeeNode(Node):
    def __init__(self, key, name, conv):
        super().__init__(key)
        self.name = name
        self.conv = conv
        self.invited = -math.inf
        self.uninvited = -math.inf

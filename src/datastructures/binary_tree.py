class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))


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

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key and self.data == other.data and \
                   self.left == other.left and self.right == other.right
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

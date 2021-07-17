from datastructures.array import Array
from datastructures.rooted_tree import RootedTree

in_memory_node_ids = set()
unsaved_node_ids = set()


class BTree(RootedTree):
    pass


class Node:
    def __init__(self, t=2):
        in_memory_node_ids.add(id(self))
        self.n = 0
        # temporarily make the node internal to safely initialize key and c attributes, then change to leaf
        self.leaf = False
        self.key = GuardedArray([None] * (2 * t - 1), id(self))
        self.c = GuardedArray([None] * (2 * t), id(self))
        self.leaf = True

    def __getattribute__(self, name):
        if id(self) not in in_memory_node_ids:
            raise AttributeError("Attempted to read an attribute of a node before reading it from disk")
        if name == "c" and self.leaf:
            raise AttributeError("Attempted to read children in a leaf")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if id(self) not in in_memory_node_ids:
            raise AttributeError("Attempted to write an attribute of a node before reading it from disk")
        if name == "c" and self.leaf:
            raise AttributeError("Attempted to write children in a leaf")
        unsaved_node_ids.add(id(self))
        super().__setattr__(name, value)


class GuardedArray(Array):
    """Meant to use as a type of key and c attributes in BTree nodes. Ensures that setting an item in its instance will
    require the owning node to be saved on disk."""

    def __init__(self, elements, node_id):
        super(GuardedArray, self).__init__(elements, start=1)
        self.node_id = node_id

    def __setitem__(self, index, item):
        unsaved_node_ids.add(self.node_id)
        super().__setitem__(index, item)


class Tree234(BTree):
    pass


class Node234:
    def __init__(self):
        self.n = 0
        self.height = 0
        self.key = Array.indexed(1, 3)
        super().__setattr__("c", Array.indexed(1, 4))

    def __getattribute__(self, name):
        if name == "c" and self.height == 0:
            raise AttributeError("Attempted to read children in a leaf")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if name == "c" and self.height == 0:
            raise AttributeError("Attempted to write children in a leaf")
        super().__setattr__(name, value)


def disk_read(x):
    in_memory_node_ids.add(id(x))


def disk_write(x):
    unsaved_node_ids.remove(id(x))


def allocate_node(t=2):
    return Node(t)


def free_node(x):
    try:
        in_memory_node_ids.remove(id(x))
        unsaved_node_ids.remove(id(x))
    except KeyError:
        pass
    del x

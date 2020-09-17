from datastructures.rooted_tree import RootedTree

nodes_in_memory = set()
nodes_unsaved = set()


class BTree(RootedTree):
    pass


class Node:
    def __init__(self):
        self.n = 0
        self.key = None
        self.leaf = False
        self.c = None

    def __getattribute__(self, name):
        if self not in nodes_in_memory:
            raise AttributeError("Attempted to read an attribute of a node before reading it from disk")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if self not in nodes_in_memory:
            raise AttributeError("Attempted to change an attribute of a node before reading it from disk")
        nodes_unsaved.add(self)
        super().__setattr__(name, value)


def disk_read(x):
    print("Reading node from disk")
    nodes_in_memory.add(x)


def disk_write(x):
    print("Writing node to disk")
    nodes_unsaved.remove(x)


def allocate_node():
    print("Allocating one disk page for a new node")
    x = Node()
    nodes_in_memory.add(x)
    return x

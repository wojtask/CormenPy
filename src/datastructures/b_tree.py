from datastructures.array import Array
from datastructures.rooted_tree import RootedTree

in_memory_node_ids = set()
unsaved_node_ids = set()


class BTree(RootedTree):
    pass


class Node:
    def __getattribute__(self, name):
        if id(self) not in in_memory_node_ids:
            raise AttributeError("Attempted to read an attribute of a node before reading it from disk")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if id(self) not in in_memory_node_ids:
            raise AttributeError("Attempted to change an attribute of a node before reading it from disk")
        unsaved_node_ids.add(id(self))
        super().__setattr__(name, value)


def disk_read(x):
    in_memory_node_ids.add(id(x))


def disk_write(x):
    unsaved_node_ids.remove(id(x))


def allocate_node(t=2):
    x = Node()
    in_memory_node_ids.add(id(x))
    x.key = Array.indexed(1, 2 * t - 1)
    x.c = Array.indexed(1, 2 * t)
    return x

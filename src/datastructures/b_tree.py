from datastructures.rooted_tree import RootedTree

in_memory_nodes = set()
unsaved_nodes = set()


class BTree(RootedTree):
    pass


class Node:
    def __getattribute__(self, name):
        if self not in in_memory_nodes:
            raise AttributeError("Attempted to read an attribute of a node before reading it from disk")
        return super().__getattribute__(name)

    def __setattr__(self, name, value):
        if self not in in_memory_nodes:
            raise AttributeError("Attempted to change an attribute of a node before reading it from disk")
        unsaved_nodes.add(self)
        super().__setattr__(name, value)


def disk_read(x):
    print("Reading node from disk")
    in_memory_nodes.add(x)


def disk_write(x):
    print("Writing node to disk")
    unsaved_nodes.remove(x)


def allocate_node():
    print("Allocating one disk page for a new node")
    x = Node()
    in_memory_nodes.add(x)
    return x

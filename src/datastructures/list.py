class List:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, key):
        self.key = key
        self.prev = self.next = None


class SNode:
    def __init__(self, key):
        self.key = key
        self.next = None


class XorList:
    def __init__(self):
        self.head = self.tail = None
        self.addr_to_node = {0: None}


class XorNode:
    def __init__(self, key, xor_list):
        self.key = key
        self.np = 0
        xor_list.addr_to_node[id(self)] = self

from datastructures.array import Array


class SinglyLinkedNode:
    def __init__(self, key):
        self.key = key
        self.next = None

    def __repr__(self):
        return self.key


class DoublyLinkedNode:
    def __init__(self, key):
        self.key = key
        self.prev = None
        self.next = None

    def __repr__(self):
        return self.key


class List:
    """Represents a list, either singly or doubly linked, either straight or circular."""

    def __init__(self):
        self.head = None

    def __iter__(self):
        if self.head is None:
            return
        yield self.head
        node = self.head.next
        while node is not None and node is not self.head:
            yield node
            node = node.next

    def __repr__(self):
        return str(list(node.key for node in self))

    def as_nodes_array(self):
        return Array(self)

    def as_keys_array(self):
        return Array(node.key for node in self)


class ListWithSentinel:
    """Represents a list with a sentinel. Can be either straight singly linked or circular doubly linked."""

    def __init__(self, singly_linked=False):
        if singly_linked:
            self.nil = SinglyLinkedNode(None)
            self.nil.next = self.nil
            self.head = self.nil
        else:
            self.nil = DoublyLinkedNode(None)
            self.nil.prev = self.nil.next = self.nil

    def __iter__(self):
        node = self.head if hasattr(self, 'head') else self.nil.next
        while node is not self.nil:
            yield node
            node = node.next

    def __repr__(self):
        return str(list(node.key for node in self))

    def as_nodes_array(self):
        return Array(self)

    def as_keys_array(self):
        return Array(node.key for node in self)


class XORNode:
    def __init__(self, key, xor_list):
        self.key = key
        self.np = 0
        xor_list.addr_to_node[id(self)] = self


class XORList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.addr_to_node = {0: None}

    def __iter__(self):
        prev_node = None
        curr_node = self.head
        while curr_node is not None:
            yield curr_node
            next_node_addr = curr_node.np ^ (id(prev_node) if prev_node is not None else 0)
            next_node = self.addr_to_node[next_node_addr]
            prev_node = curr_node
            curr_node = next_node

    def __repr__(self):
        return str(list(node.key for node in self))

    def as_nodes_array(self):
        return Array(self)

    def as_keys_array(self):
        return Array(node.key for node in self)

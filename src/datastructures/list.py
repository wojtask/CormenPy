from datastructures.array import Array
from datastructures.essential import Element


class SinglyLinkedNode(Element):
    def __init__(self, key, data=None):
        super().__init__(key, data)
        self.next = None


class DoublyLinkedNode(Element):
    def __init__(self, key, data=None):
        super().__init__(key, data)
        self.prev = None
        self.next = None


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


class ListWithTail(List):
    def __init__(self):
        super().__init__()
        self.tail = None


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


class SingleArrayList:
    def __init__(self, A, head, free):
        self.A = A
        self.head = head
        self.free = free

    def __iter__(self):
        idx = self.head
        while idx is not None:
            yield self.A[idx]
            idx = self.A[idx + 1]

    def get_free_list_size(self):
        idx = self.free
        free_cells = 0
        while idx is not None:
            free_cells += 1
            idx = self.A[idx + 1]
        return free_cells


class MultipleArrayList:
    def __init__(self, key, next, prev, head, free):
        self.key = key
        self.next = next
        self.prev = prev
        self.head = head
        self.free = free

    def __iter__(self):
        idx = self.head
        while idx is not None:
            yield self.key[idx]
            idx = self.next[idx]

    def get_free_list_size(self):
        idx = self.free
        free_cells = 0
        while idx is not None:
            free_cells += 1
            idx = self.next[idx]
        return free_cells

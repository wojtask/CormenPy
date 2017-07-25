class List:
    def __init__(self):
        self.head = None


class Node:
    def __init__(self, key):
        self.key = key
        self.prev = self.next = None

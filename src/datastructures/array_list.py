class MultipleArrayList:
    def __init__(self, key, next, prev, head, free):
        self.key = key
        self.next = next
        self.prev = prev
        self.head = head
        self.free = free


class SingleArrayList:
    def __init__(self, A, head, free):
        self.A = A
        self.head = head
        self.free = free

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

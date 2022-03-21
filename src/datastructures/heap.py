from datastructures.array import Array


class Heap(Array):
    def __init__(self, elements, heap_size=0):
        super().__init__(elements)
        self.heap_size = heap_size

    def __getitem__(self, index):
        if not isinstance(index, int):
            TypeError('Cannot address Heap with indexes other than int')
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            TypeError('Cannot address Heap with indexes other than int')
        return super().__setitem__(index, value)

    def __len__(self):
        return self.heap_size

    def __iter__(self):
        return iter(super().__getitem__(slice(None, self.heap_size)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return list(iter(self)) == list(iter(other))
        return NotImplemented

    def __repr__(self):
        return str(list(iter(self)))

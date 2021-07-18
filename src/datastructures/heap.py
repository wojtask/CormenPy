from datastructures.array import Array


class Heap(Array):
    def __init__(self, elements):
        super().__init__(elements)
        self.heap_size = len(elements)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.heap_size == other.heap_size and self.elements[:self.heap_size] == other.elements[
                                                                                           :other.heap_size]
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.heap_size, self.elements[:self.heap_size]))

    def __len__(self):
        return self.heap_size

    def __iter__(self):
        return (item for item in self.elements[:self.heap_size])

    def __contains__(self, item):
        return item in self.elements[:self.heap_size]

    def __str__(self):
        return self.elements[:self.heap_size]

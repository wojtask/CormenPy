from datastructures.array import Array


class Heap(Array):
    def __init__(self, data):
        super().__init__(data)
        self.heap_size = len(data)

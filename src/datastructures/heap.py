from datastructures.array import Array


class Heap(Array):
    def __init__(self, data):
        Array.__init__(self, data)
        self.heap_size = len(data)

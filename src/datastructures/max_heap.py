from datastructures.array import Array


class MaxHeap(Array):
    def __init__(self, data):
        Array.__init__(self, data)
        self.heap_size = len(data)

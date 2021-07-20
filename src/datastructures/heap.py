from datastructures.array import Array


class Heap(Array):
    def __init__(self, *elements):
        super().__init__(*elements)
        self.heap_size = self.length

    def __getitem__(self, index):
        if not isinstance(index, int):
            TypeError('Cannot address Heap with indexes other than int')
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            TypeError('Cannot address Heap with indexes other than int')
        return super().__setitem__(index, value)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return [element for element in self] == [element for element in other]
        return NotImplemented

    def __len__(self):
        return self.heap_size

    def __iter__(self):
        return (element for element in self.elements[:self.heap_size])

    def __repr__(self):
        return str([element for element in self])

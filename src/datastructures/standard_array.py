from builtins import len


# a 0-based indexed (standard) array
class StandardArray:
    def __init__(self, elements):
        self.elements = list(elements)
        self.length = len(elements)

    @classmethod
    def of_length(cls, length):
        return cls([None] * length)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.elements[index]
        return StandardArray(self.elements[index.start:index.stop + 1])

    def __setitem__(self, index, item):
        self.elements[index] = item

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.length == other.length and self.elements == other.elements
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.length, self.elements))

    def __iter__(self):
        return (x for x in self.elements)

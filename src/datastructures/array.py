from builtins import len


# a 1-based indexed array
class Array:
    def __init__(self, data):
        self.data = list(data)
        self.length = len(data)

    @classmethod
    def of_length(cls, length):
        return cls([None] * length)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.data[index - 1]
        return Array(self.data[index.start - 1:index.stop])

    def __setitem__(self, index, item):
        self.data[index - 1] = item

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.length == other.length and self.data == other.data
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.length, self.data))

    def __iter__(self):
        return (x for x in self.data)

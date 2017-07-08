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
        return self.data[index - 1]

    def __setitem__(self, index, item):
        self.data[index - 1] = item

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))

    def __iter__(self):
        return (x for x in self.data)

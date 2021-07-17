from builtins import len


class Array:
    def __init__(self, elements, start=1):
        self.elements = list(elements)
        self.start = start
        self.length = len(elements)

    @classmethod
    def indexed(cls, _from, _to):
        return cls([None] * (_to - _from + 1), start=_from)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.elements[index - self.start]
        if isinstance(index, tuple):
            row = self.elements[index[0] - self.start]
            return row.elements[index[1] - row.start]
        start = index.start if index.start is not None else self.start
        stop = index.stop if index.stop is not None else self.length
        if start < self.start or stop - self.start + 1 > self.length:
            raise IndexError('Invalid indexes used when addressing Array')
        return Array(self.elements[start - self.start:stop - self.start + 1], start=start)

    def __setitem__(self, index, item):
        if isinstance(index, int):
            self.elements[index - self.start] = item
        else:
            row = self.elements[index[0] - self.start]
            row.elements[index[1] - row.start] = item

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.length == other.length and self.start == other.start and self.elements[:self.length] == \
                   other.elements[:other.length]
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self):
        return hash((self.length, self.start, self.elements[:self.length]))

    def __iter__(self):
        return (item for item in self.elements)

    def __contains__(self, item):
        return item in self.elements

    def __str__(self):
        return "%s indexed from %d" % (self.elements[:self.length], self.start)

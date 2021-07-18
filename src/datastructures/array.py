from builtins import len


class Array:
    def __init__(self, elements=None, start=1):
        self.elements = list(elements or [])
        self.length = len(self.elements)
        self.start = start

    @classmethod
    def indexed(cls, _from, _to):
        return cls([None] * (_to - _from + 1), start=_from)

    def __getitem__(self, index):
        if isinstance(index, int):
            return self.elements[index - self.start]
        if isinstance(index, slice):
            start = index.start if index.start is not None else self.start
            stop = index.stop if index.stop is not None else self.length
            if start < self.start or stop - self.start + 1 > self.length:
                raise IndexError('Invalid indexes used for addressing Array')
            return Array(self.elements[start - self.start:stop - self.start + 1], start=self.start)
        if isinstance(index, tuple):
            row = self.elements[index[0] - self.start]
            return row.elements[index[1] - row.start]
        raise IndexError('Invalid type of index used for indexing Array')

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

    def __bool__(self):
        return self.length > 0

    def __len__(self):
        return self.length

    def __iter__(self):
        return (item for item in self.elements)

    def __contains__(self, item):
        return item in self.elements

    def __reversed__(self):
        return Array(list(reversed(self.elements)), start=self.start)

    def __add__(self, other):
        return Array(self.elements + other.elements, start=self.start)

    def __str__(self):
        return '%s indexed from %d' % (self.elements[:self.length], self.start)

    def sort(self, **kwargs):
        return Array(sorted(self.elements, **kwargs), start=self.start)

    def index(self, value, start=None):
        if start:
            return self.elements.index(value, start - self.start) + self.start
        return self.elements.index(value) + self.start

    def count(self, value):
        return sum(1 for v in self if v is value or v == value)

    def append(self, value):
        self.length += 1
        if self.length < len(self.elements):
            self.elements[self.length] = value
        else:
            self.elements.append(value)

    def insert(self, index, value):
        self.elements.insert(index - self.start, value)
        self.length += 1

    def pop(self, index):
        value = self.elements.pop(index - self.start)
        self.length -= 1
        return value

    def remove(self, value):
        if self.elements.index(value) >= self.length:
            raise ValueError('Array doesn\'t have the requested value')
        self.elements.remove(value)
        self.length -= 1

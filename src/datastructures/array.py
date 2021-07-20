import random
from builtins import len
from collections.abc import MutableSequence


class Array(MutableSequence):
    def __init__(self, elements=None, start=1):
        self.elements = list(elements or [])
        self.length = len(self.elements)
        self.start = start

    @classmethod
    def indexed(cls, _from, _to):
        return cls([None] * (_to - _from + 1), start=_from)

    def __getitem__(self, index):
        if isinstance(index, int):
            if index < self.start or index > self.length:
                raise IndexError('Invalid index used for addressing Array')
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
        raise TypeError('Invalid type of index used for indexing Array')

    def __setitem__(self, index, value):
        if isinstance(index, int):
            self.elements[index - self.start] = value
        elif isinstance(index, tuple):
            row = self.elements[index[0] - self.start]
            row.elements[index[1] - row.start] = value
        else:
            raise TypeError('Invalid type of index used for indexing Array')

    def __delitem__(self, index):
        del self.elements[index - self.start]
        self.length -= 1

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.start == other.start and [element for element in self] == [element for element in other]
        return NotImplemented

    def __len__(self):
        return self.length

    def __bool__(self):
        return self.length > 0

    def __iter__(self):
        return (element for element in self.elements[:self.length])

    def __reversed__(self):
        return reversed([element for element in self])

    def __add__(self, other):
        return Array([element for element in self] + [element for element in other], start=self.start)

    def __repr__(self):
        return '%s indexed from %d' % ([element for element in self], self.start)

    def index(self, value, start=None, stop=None):
        if start is None:
            start = self.start
        return super().index(value, start)

    def insert(self, index, value):
        self.elements.insert(index - self.start, value)
        self.length += 1

    def append(self, value):
        self.insert(self.length + 1, value)

    def sort(self, **kwargs):
        self.elements.sort(**kwargs)
        return self

    def shuffle(self):
        random.shuffle(self.elements)
        return self

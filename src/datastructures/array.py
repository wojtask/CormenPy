import random
from builtins import len
from collections.abc import MutableSequence

from util import between


class Array(MutableSequence):
    def __init__(self, *elements, **kwargs):
        self.elements = []
        for element in elements:
            try:
                iter(element)
                self.elements.extend(list(element) or [])
            except TypeError:
                self.elements.append(element)
        self.length = len(self.elements)
        self.start = kwargs['start'] if 'start' in kwargs else 1

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
            return Array((self[i] for i in between(start, stop)), start=self.start)
        if isinstance(index, tuple):
            return self[index[0]][index[1]]
        raise TypeError('Invalid type of index used for indexing Array')

    def __setitem__(self, index, value):
        if isinstance(index, int):
            if index < self.start or index > self.length:
                raise IndexError('Invalid index used for updating an Array\'s cell')
            self.elements[index - self.start] = value
        elif isinstance(index, slice):
            it = iter(value)
            start = index.start if index.start is not None else self.start
            stop = index.stop if index.stop is not None else self.length
            if len(value) != stop - start + 1:
                raise IndexError('The iterable used for updating an Array\'s fragment has different size')
            for i in between(start, stop):
                self[i] = next(it)
        elif isinstance(index, tuple):
            self[index[0]][index[1]] = value
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

    def __iter__(self):
        return (element for element in self.elements[:self.length])

    def __reversed__(self):
        return (rev for rev in reversed([element for element in self]))

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

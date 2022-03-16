from datastructures.array import Array


class Queue(Array):
    def __init__(self, *elements, head=1, tail=1):
        if head < 1 or head > len(*elements):
            raise IndexError('Invalid head attribute')
        if tail < 1 or tail > len(*elements):
            raise IndexError('Invalid tail attribute')
        super().__init__(*elements)
        self.head = head
        self.tail = tail

    def __getitem__(self, index):
        if not isinstance(index, int):
            TypeError('Cannot address Queue with indexes other than int')
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            TypeError('Cannot address Queue with indexes other than int')
        return super().__setitem__(index, value)

    def __len__(self):
        if self.head <= self.tail:
            return self.tail - self.head
        return self.length - self.head + self.tail

    def __iter__(self):
        if self.head <= self.tail:
            return iter(super().__getitem__(slice(self.head, self.tail - 1)))
        return iter(super().__getitem__(slice(self.head, None)) + super().__getitem__(slice(None, self.tail - 1)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return list(iter(self)) == list(iter(other))
        return NotImplemented

    def __repr__(self):
        return str(list(iter(self)))

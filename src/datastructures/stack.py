from datastructures.array import Array


class Stack(Array):
    def __init__(self, elements, top=0):
        if top < 0 or top > len(elements):
            raise IndexError('Invalid top attribute')
        super().__init__(elements)
        self.top = top

    def __getitem__(self, index):
        if not isinstance(index, int):
            TypeError('Cannot address Stack with indexes other than int')
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if not isinstance(index, int):
            TypeError('Cannot address Stack with indexes other than int')
        return super().__setitem__(index, value)

    def __len__(self):
        return self.top

    def __iter__(self):
        return reversed(super().__getitem__(slice(None, self.top)))

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return list(iter(self)) == list(iter(other))
        return NotImplemented

    def __repr__(self):
        return str(list(iter(self)))


class DoubleStack(Array):
    def __init__(self, elements, left_top, right_top):
        super().__init__(elements)
        self.left_top = left_top
        self.right_top = right_top

    def get_left_stack_elements(self):
        return self[:self.left_top]

    def get_right_stack_elements(self):
        return self[self.right_top:]

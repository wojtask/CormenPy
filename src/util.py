from builtins import range


def between(start, end, step=1):
    return range(start, end + 1, step)


def rbetween(start, end):
    return range(start, end - 1, -1)


class Element:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.key == other.key and self.data == other.data
        return NotImplemented

    def __hash__(self):
        return hash((self.key, self.data))

    def __repr__(self):
        return 'Element(%d)' % self.key

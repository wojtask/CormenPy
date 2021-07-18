from builtins import range


def between(start, end):
    return range(start, end + 1)


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

    def __ne__(self, other):
        if isinstance(other, self.__class__):
            return not self.__eq__(other)
        return NotImplemented

    def __hash__(self) -> int:
        return hash((self.key, self.data))

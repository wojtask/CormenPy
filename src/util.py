from builtins import range


def between(start, end, step=1):
    return range(start, end + 1, step)


def rbetween(start, end):
    return range(start, end - 1, -1)


def ceildiv(a, b):
    return -(a // -b)


class ModificationDetectable:
    def __init__(self):
        self._modified = False

    def is_modified(self):
        return self._modified

    def save_state(self):
        self._modified = False
        return self

from builtins import range


def between(start, end):
    return range(start, end + 1)


def rbetween(start, end):
    return range(start, end - 1, -1)


class Element:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data

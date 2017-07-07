from builtins import range


def between(start, end):
    return range(start, end + 1)


def rbetween(start, end):
    return range(start, end - 1, -1)

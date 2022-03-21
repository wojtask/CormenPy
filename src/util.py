from builtins import range


def between(start, end, step=1):
    return range(start, end + 1, step)


def rbetween(start, end):
    return range(start, end - 1, -1)

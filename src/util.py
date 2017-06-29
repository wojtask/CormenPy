from builtins import range


def scope(start, end):
    return range(start, end + 1)


def rscope(start, end):
    return range(start, end - 1, -1)

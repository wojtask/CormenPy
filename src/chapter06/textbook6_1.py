import math


def parent(i):
    return math.floor(i / 2)


def left(i):
    return 2 * i


def right(i):
    return 2 * i + 1

from random import randrange


def random(a, b):
    while a < b:
        mid = (a + b) // 2
        if _random() == 0:
            a = mid + 1
        else:
            b = mid
    return a


def _random():
    return randrange(2)

import math
from random import randint


def random(a, b):
    if a == 0 and b == 1:
        return randint(0, 1)
    while a < b:
        mid = math.floor((a + b) / 2)
        if random(0, 1) == 0:
            a = mid + 1
        else:
            b = mid
    return a

from datastructures.array import Array
from util import between


class ResettableCounter(Array):
    def __init__(self, *elements):
        super().__init__(*elements, start=0)
        self.highest = -1


def increment_(A):
    i = 0
    while i < A.length and A[i] == 1:
        A[i] = 0
        i += 1
    if i < A.length:
        A[i] = 1
        if i > A.highest:
            A.highest = i
    else:
        A.highest = -1


def reset(A):
    for i in between(0, A.highest):
        A[i] = 0
    A.highest = -1

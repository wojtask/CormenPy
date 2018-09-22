from util import between


def reset(A):
    for i in between(0, A.highest):
        A[i] = 0
    A.highest = None

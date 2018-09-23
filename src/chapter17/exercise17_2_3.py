from util import between


def increment_(A):
    i = 0
    while i < A.length and A[i] == 1:
        A[i] = 0
        i = i + 1
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

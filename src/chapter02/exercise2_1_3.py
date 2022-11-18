from util import between


def linear_search(A, v):
    for i in between(1, A.length):
        if A[i] == v:
            return i
    return None

from chapter10.textbook10_1 import stack_empty, pop


def multipop(S, k):
    while not stack_empty(S) and k != 0:
        pop(S)
        k = k - 1


def increment(A):
    i = 0
    while i < A.length and A[i] == 1:
        A[i] = 0
        i = i + 1
    if i < A.length:
        A[i] = 1

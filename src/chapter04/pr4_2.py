from datastructures.array import Array


def getbit(a, j):
    return 1 if a & (1 << j) else 0


def find_missing_integer(A):
    n = A.length
    missing = 0
    j = 0
    while n > 0:
        zeros = [a for a in A.data if getbit(a, j) == 0]
        ones = [a for a in A.data if getbit(a, j) == 1]
        if len(zeros) == n // 2 + 1:
            A = Array(ones)
            missing |= (1 << j)
        else:
            A = Array(zeros)
        n = A.length
        j += 1
    return missing

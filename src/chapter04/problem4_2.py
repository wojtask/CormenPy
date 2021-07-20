from datastructures.array import Array


def missing_integer(A):
    n = A.length
    missing = 0
    j = 0
    while n > 0:
        zeros = Array(a for a in A if _get_bit(a, j) == 0)
        ones = Array(a for a in A if _get_bit(a, j) == 1)
        if zeros.length == n // 2 + 1:
            A = ones
            missing |= (1 << j)
        else:
            A = zeros
        n = A.length
        j += 1
    return missing


def _get_bit(a, j):
    return 1 if a & (1 << j) else 0

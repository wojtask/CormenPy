from chapter07.textbook7_3 import randomized_partition


def iterative_randomized_select(A, p, r, i):
    while p < r:
        q = randomized_partition(A, p, r)
        k = q - p + 1
        if i == k:
            return A[q]
        if i < k:
            r = q - 1
        else:
            p = q + 1
            i = i - k
    return A[p]

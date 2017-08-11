from util import between


def randomly_built_tree_quicksort(A, p, r):
    if p < r:
        q = _randomly_built_tree_partition(A, p, r)
        randomly_built_tree_quicksort(A, p, q - 1)
        randomly_built_tree_quicksort(A, q + 1, r)


def _randomly_built_tree_partition(A, p, r):
    x = A[p]
    i = p
    for j in between(p + 1, r):
        if A[j] < x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i], A[p] = A[p], A[i]
    return i

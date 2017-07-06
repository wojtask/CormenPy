from chapter07.textbook import hoare_partition


def hoare_quicksort(A, p, r):
    if p < r:
        q = hoare_partition(A, p, r)
        hoare_quicksort(A, p, q)
        hoare_quicksort(A, q + 1, r)

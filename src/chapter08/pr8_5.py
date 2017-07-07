from chapter07.textbook import partition


def average_sort(A, k, p, r):
    if p + k - 1 < r:
        q = partition(A, p, r)
        average_sort(A, k, p, q - 1)
        average_sort(A, k, q + 1, r)

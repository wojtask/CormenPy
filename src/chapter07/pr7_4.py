from chapter07.textbook import partition


def quicksort__(A, p, r):
    while p < r:
        q = partition(A, p, r)
        if q - p < r - q:
            quicksort__(A, p, q - 1)
            p = q + 1
        else:
            quicksort__(A, q + 1, r)
            r = q - 1

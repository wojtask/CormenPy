from chapter07.textbook7_1 import partition


def quicksort_(A, p, r):
    while p < r:
        q = partition(A, p, r)
        quicksort_(A, p, q - 1)
        p = q + 1

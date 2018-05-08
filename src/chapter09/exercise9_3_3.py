from chapter09.textbook9_3 import select


def best_case_quicksort(A, p, r):
    if p < r:
        n = r - p + 1
        select(A, p, r, (n + 1) // 2)
        q = (p + r) // 2
        best_case_quicksort(A, p, q - 1)
        best_case_quicksort(A, q + 1, r)

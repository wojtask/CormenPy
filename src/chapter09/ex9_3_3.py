from chapter09.textbook import select


def best_case_quicksort(A, p, r):
    if p < r:
        q = (p + r) // 2
        select(A, p, r, q)
        best_case_quicksort(A, p, q - 1)
        best_case_quicksort(A, q + 1, r)

from chapter02.textbook2_1 import insertion_sort
from chapter07.textbook7_1 import partition


def insertion_quicksort(A, p, r, k):
    if p < r:
        if r - p + 1 >= k:
            q = partition(A, p, r)
            insertion_quicksort(A, p, q - 1, k)
            insertion_quicksort(A, q + 1, r, k)
        else:
            nearly_sorted = A[p:r]
            insertion_sort(nearly_sorted)
            A[p:r] = nearly_sorted

from chapter07.textbook7_1 import quicksort


def sets_reordering(A, B):
    quicksort(A, 1, A.length)
    quicksort(B, 1, B.length)

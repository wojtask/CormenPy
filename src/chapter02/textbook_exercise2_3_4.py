def recursive_insertion_sort(A, n):
    if n > 1:
        recursive_insertion_sort(A, n - 1)
    key = A[n]
    i = n - 1
    while i > 0 and A[i] > key:
        A[i + 1] = A[i]
        i -= 1
    A[i + 1] = key

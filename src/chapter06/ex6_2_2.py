from chapter06.textbook import left, right


def min_heapify(A, i):
    l = left(i)
    r = right(i)
    if l <= A.heap_size and A[l] < A[i]:
        smallest = l
    else:
        smallest = i
    if r <= A.heap_size and A[r] < A[smallest]:
        smallest = r
    if smallest != i:
        A[i], A[smallest] = A[smallest], A[i]
        min_heapify(A, smallest)

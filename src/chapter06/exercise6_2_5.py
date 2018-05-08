from chapter06.textbook6_1 import left, right


def iterative_max_heapify(A, i):
    while True:
        l = left(i)
        r = right(i)
        if l <= A.heap_size and A[l] > A[i]:
            largest = l
        else:
            largest = i
        if r <= A.heap_size and A[r] > A[largest]:
            largest = r
        if largest == i:
            return
        A[i], A[largest] = A[largest], A[i]
        i = largest

from chapter09.textbook import select
from datastructures.array import Array
from datastructures.point_2d import Point2D
from util import between


def weighted_median_using_sorting(A, w):
    _sort_array_with_weights(A, w)
    weight_sum = 0.0
    i = 1
    while i <= A.length and weight_sum < 1/2:
        weight_sum += w[i]
        i += 1
    return A[i - 1]


def _sort_array_with_weights(A, w):
    array_with_weights = sorted(zip(A, w), key=lambda x: x[0])
    A.data = [x[0] for x in array_with_weights]
    w.data = [x[1] for x in array_with_weights]


def weighted_median(A, w, p, r):
    if r - p + 1 <= 2:
        if w[p] >= w[r]:
            return A[p]
        else:
            return A[r]
    _partition_around_median(A, w, p, r)
    q = (p + r) // 2
    WL = 0.0
    for i in between(p, q - 1):
        WL = WL + w[i]
    WR = 1 - WL - w[q]
    if WL < 1/2 and WR < 1/2:
        return A[q]
    if WL >= 1/2:
        w[q] = w[q] + WR
        return weighted_median(A, w, p, q)
    else:
        w[q] = w[q] + WL
        return weighted_median(A, w, q, r)


def _partition_around_median(A, w, p, r):
    median = select(Array(A.data), p, r, (p + r) // 2)  # we pass a copy of A because it will be modified in select
    q = p
    while A[q] != median:
        q += 1
    A[q], A[r] = A[r], A[q]
    w[q], w[r] = w[r], w[q]
    i = p - 1
    for j in between(p, r - 1):
        if A[j] < median:
            i = i + 1
            A[i], A[j] = A[j], A[i]
            w[i], w[j] = w[j], w[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    w[i + 1], w[r] = w[r], w[i + 1]
    return i + 1


def post_office_manhattan(A, w):
    X = Array([p.x for p in A.data])
    Y = Array([p.y for p in A.data])
    post_office_x = weighted_median(X, Array(w.data), 1, X.length)
    post_office_y = weighted_median(Y, Array(w.data), 1, Y.length)
    return Point2D(post_office_x, post_office_y)

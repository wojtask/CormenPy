from chapter09.textbook9_3 import select
from chapter10.textbook10_2 import list_insert, list_delete
from datastructures.array import Array


def _transform_to_array(S):
    elements = []
    x = S.head
    while x is not None:
        elements.append(x.key)
        x = x.next
    return Array(elements)


def dlh_insert(S, x):
    list_insert(S, x)


def delete_larger_half(S):
    A = _transform_to_array(S)
    M = select(A, 1, A.length, (A.length + 1) // 2)
    size = A.length
    x = S.head
    while x is not None:
        if x.key > M:
            list_delete(S, x)
            size -= 1
        x = x.next
    x = S.head
    while size > A.length // 2:
        if x.key == M:
            list_delete(S, x)
            size -= 1
        x = x.next

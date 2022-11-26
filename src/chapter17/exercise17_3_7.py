from chapter09.textbook9_3 import select
from chapter10.textbook10_2 import list_insert, list_delete
from datastructures.array import Array
from util import ceildiv


def _transform_to_array(S):
    A = Array()
    x = S.head
    while x is not None:
        A.append(x.key)
        x = x.next
    return A


def dlh_insert(S, x):
    list_insert(S, x)


def delete_larger_half(S):
    A = _transform_to_array(S)
    M = select(A, 1, A.length, (A.length + 1) // 2)
    deleted = 0
    x = S.head
    while x is not None:
        if x.key > M:
            list_delete(S, x)
            deleted += 1
        x = x.next
    x = S.head
    while deleted < ceildiv(A.length, 2):
        if x.key == M:
            list_delete(S, x)
            deleted += 1
        x = x.next

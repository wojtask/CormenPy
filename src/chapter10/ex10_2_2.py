from chapter10.ex10_2_1 import singly_linked_list_insert
from datastructures.list import SNode


def singly_linked_list_push(L, k):
    x = SNode(None)
    x.key = k
    singly_linked_list_insert(L, x)


def singly_linked_list_pop(L):
    if L.head is None:
        raise RuntimeError('underflow')
    x = L.head
    L.head = x.next
    return x.key

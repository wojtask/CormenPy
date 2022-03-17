from chapter10.exercise10_2_1 import singly_linked_list_insert
from datastructures.list import SinglyLinkedNode


def singly_linked_list_push(L, k):
    x = SinglyLinkedNode(None)
    x.key = k
    singly_linked_list_insert(L, x)


def singly_linked_list_pop(L):
    if L.head is None:
        raise ValueError('underflow')
    x = L.head
    L.head = x.next
    return x.key

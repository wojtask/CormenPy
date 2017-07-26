from chapter10.ex10_2_1 import singly_linked_list_delete, singly_linked_list_insert
from datastructures.list import List


def singly_linked_list_reverse(L):
    L_ = List()
    L_.head = None
    while L.head is not None:
        x = L.head
        singly_linked_list_delete(L, L.head)
        singly_linked_list_insert(L_, x)
    L.head = L_.head

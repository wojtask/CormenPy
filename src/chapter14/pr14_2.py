from chapter10.ex10_2_1 import singly_linked_list_insert
from chapter14.textbook import os_insert, os_select, os_delete
from datastructures.list import List, SNode
from datastructures.red_black_tree import RedBlackTree, OSNode
from util import between, rbetween


def josephus_simulate(n, m):
    L = List()
    singly_linked_list_insert(L, SNode(n))
    x = L.head
    for i in rbetween(n - 1, 1):
        singly_linked_list_insert(L, SNode(i))
    x.next = L.head
    for i in between(1, n):
        for j in between(1, m):
            x = x.next
        print(x.next.key)
        if L.head is x.next:
            L.head = x.next.next
        x.next = x.next.next


def josephus(n, m):
    T = RedBlackTree(sentinel=OSNode(None))
    for j in between(1, n):
        x = OSNode(j)
        os_insert(T, x)
    j = 1
    for k in rbetween(n, 1):
        j = (j + m - 1) % k + 1
        x = os_select(T.root, j)
        print(x.key)
        os_delete(T, x)

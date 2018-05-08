from datastructures.list import SNode


def singly_linked_list_enqueue(L, k):
    x = SNode(None)
    x.next = None
    x.key = k
    if L.tail is not None:
        L.tail.next = x
    else:
        L.head = x
    L.tail = x


def singly_linked_list_dequeue(L):
    if L.head is None:
        raise RuntimeError('underflow')
    x = L.head
    L.head = x.next
    if L.tail is x:
        L.tail = None
    return x.key

from datastructures.list import List


def circular_lists_union(S1, S2):
    S = List()
    if S1.head is not None and S2.head is not None:
        x = S1.head.next
        S1.head.next = S2.head.next
        S2.head.next = x
    if S1.head is not None:
        S.head = S1.head
    else:
        S.head = S2.head
    S1.head = S2.head = None
    return S

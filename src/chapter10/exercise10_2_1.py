def singly_linked_list_insert(L, x):
    x.next = L.head
    L.head = x


def singly_linked_list_delete(L, x):
    if x is L.head:
        L.head = L.head.next
    else:
        y = L.head
        while y.next is not x:
            y = y.next
        y.next = x.next

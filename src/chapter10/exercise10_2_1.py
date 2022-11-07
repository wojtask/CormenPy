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


def singly_linked_list_delete_(L, x):
    if x.next is not None:
        x.key = x.next.key
        x.data = x.next.data
        x.next = x.next.next
    else:
        singly_linked_list_delete(L, x)

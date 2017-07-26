def circular_list_insert(L, x):
    if L.head is None:
        L.head = x.next = x
    else:
        x.next = L.head.next
        L.head.next = x


def circular_list_delete(L, x):
    y = L.head
    while y.next is not x:
        y = y.next
    y.next = x.next
    if L.head is x:
        if x.next is x:
            L.head = None
        else:
            L.head = x.next


def circular_list_search(L, k):
    if L.head is None:
        return None
    if L.head.key == k:
        return L.head
    x = L.head.next
    while x is not L.head:
        if x.key == k:
            return x
        x = x.next
    return None

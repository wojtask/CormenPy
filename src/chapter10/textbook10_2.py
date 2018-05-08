def list_search(L, k):
    x = L.head
    while x is not None and x.key != k:
        x = x.next
    return x


def list_insert(L, x):
    x.next = L.head
    if L.head is not None:
        L.head.prev = x
    L.head = x
    x.prev = None


def list_delete(L, x):
    if x.prev is not None:
        x.prev.next = x.next
    else:
        L.head = x.next
    if x.next is not None:
        x.next.prev = x.prev


def list_delete_(L, x):
    x.prev.next = x.next
    x.next.prev = x.prev


def list_search_(L, k):
    x = L.nil.next
    while x is not L.nil and x.key != k:
        x = x.next
    return x


def list_insert_(L, x):
    x.next = L.nil.next
    L.nil.next.prev = x
    L.nil.next = x
    x.prev = L.nil

from datastructures.list import XorNode


def _xor(x, y):
    if x is None:
        x = 0
    elif isinstance(x, XorNode):
        x = id(x)
    if y is None:
        y = 0
    elif isinstance(y, XorNode):
        y = id(y)
    return x ^ y


def xor_linked_list_search(L, k):
    x = L.head
    y = None
    while x is not None and x.key != k:
        z = L.addr_to_node[_xor(x.np, y)]
        y = x
        x = z
    return x


def xor_linked_list_insert(L, x):
    x.np = id(L.head) if L.head is not None else 0
    if L.head is not None:
        L.head.np = _xor(L.head.np, x)
    L.head = x
    if L.tail is None:
        L.tail = x


def xor_linked_list_delete(L, x):
    x_ = L.head
    y = None
    while x_ is not x:
        z = L.addr_to_node[_xor(x_.np, y)]
        y = x_
        x_ = z
    z = L.addr_to_node[_xor(x.np, y)]
    if x is L.head:
        L.head = z
    else:
        y.np = _xor(_xor(y.np, x), z)
    if x is L.tail:
        L.tail = y
    else:
        z.np = _xor(_xor(z.np, x), y)


def xor_linked_list_reverse(L):
    L.head, L.tail = L.tail, L.head

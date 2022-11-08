def list_union(L1, L2):
    L2.nil.next.prev = L1.nil.prev
    L1.nil.prev.next = L2.nil.next
    L2.nil.prev.next = L1.nil
    L1.nil.prev = L2.nil.prev
    return L1

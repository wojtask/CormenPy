def list_search__(L, k):
    L.nil.key = k
    x = L.nil.next
    while x.key != k:
        x = x.next
    return x

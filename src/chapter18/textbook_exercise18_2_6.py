from datastructures.b_tree import disk_read


def b_tree_binary_search(x, k):
    low = 1
    high = x.n
    while low <= high:
        mid = (low + high) // 2
        if k == x.key[mid]:
            return x, mid
        if k < x.key[mid]:
            high = mid - 1
        else:
            low = mid + 1
    if x.leaf:
        return None
    else:
        disk_read(x.c[low])
        return b_tree_binary_search(x.c[low], k)

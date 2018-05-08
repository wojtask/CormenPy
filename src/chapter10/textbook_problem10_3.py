from chapter05.exercise5_1_2 import random


def compact_list_search(L, n, k):
    i = L.head
    while i is not None and L.key[i] < k:
        j = random(1, n)
        if L.key[i] < L.key[j] and L.key[j] <= k:
            i = j
            if L.key[i] == k:
                return i
        i = L.next[i]
    if i is None or L.key[i] > k:
        return None
    else:
        return i

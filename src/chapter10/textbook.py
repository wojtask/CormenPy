from chapter05.ex5_1_2 import random


def stack_empty(S):
    if S.top == 0:
        return True
    else:
        return False


def push(S, x):
    S.top = S.top + 1
    S[S.top] = x


def pop(S):
    if stack_empty(S):
        raise RuntimeError('underflow')
    else:
        S.top = S.top - 1
        return S[S.top + 1]


def enqueue(Q, x):
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 1
    else:
        Q.tail = Q.tail + 1


def dequeue(Q):
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 1
    else:
        Q.head = Q.head + 1
    return x


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


def allocate_object(L):
    if L.free is None:
        raise RuntimeError('out of space')
    else:
        x = L.free
        L.free = L.next[x]
        return x


def free_object(L, x):
    L.next[x] = L.free
    L.free = x


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

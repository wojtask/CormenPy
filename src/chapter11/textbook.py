import random

from sympy import sieve

from datastructures.array import Array


def direct_address_search(T, k):
    return T[k]


def direct_address_insert(T, x):
    T[x.key] = x


def direct_address_delete(T, x):
    T[x.key] = None


def chained_hash_insert(T, x, h):
    m = T.length
    list_ = T[h(x.key, m)]
    x.next = list_
    if list_ is not None:
        list_.prev = x
    T[h(x.key, m)] = x
    x.prev = None


def chained_hash_search(T, k, h):
    m = T.length
    x = T[h(k, m)]
    while x is not None and x.key != k:
        x = x.next
    return x


def chained_hash_delete(T, x, h):
    m = T.length
    if x.prev is not None:
        x.prev.next = x.next
    else:
        T[h(x.key, m)] = x.next
    if x.next is not None:
        x.next.prev = x.prev


def hash_insert(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i, m)
        if T[j] is None:
            T[j] = k
            return j
        else:
            i = i + 1
        if i == m:
            break
    raise RuntimeError('hash table overflow')


def hash_search(T, k, h):
    m = T.length
    i = 0
    while True:
        j = h(k, i, m)
        if T[j] == k:
            return j
        i = i + 1
        if T[j] is None or i == m:
            break
    return None


def quadratic_probing_search(T, k, h):
    m = T.length
    i = h(k, m)
    j = 0
    while True:
        if T[i] is None:
            return None
        if T[i] == k:
            return i
        j = j + 1
        if j == m:
            return None
        else:
            i = (i + j) % m


def _get_random_universal_hash_function(p, m):
    a = random.randint(1, p - 1)
    b = random.randint(0, p - 1)
    return lambda k: ((a * k + b) % p) % m


def perfect_hashing_init(K):
    max_key = max(K)
    # from Bertrand's postulate, for each n >= 1, there is a prime p, such that n < p <= 2n
    p = random.choice(list(sieve.primerange(max_key + 1, 2 * max_key + 1)))
    m = K.length
    T = Array.indexed(0, m - 1)
    h = _get_random_universal_hash_function(p, m)
    mapped_keys = [[] for _ in range(m)]
    for k in K:
        mapped_keys[h(k)].append(k)
    secondary_sizes = [len(keys) ** 2 for keys in mapped_keys]
    for j, size in enumerate(secondary_sizes):
        if size == 1:
            T[j] = (lambda _: 0, Array([mapped_keys[j][0]], start=0))
        elif size > 1:
            h_ = None
            S = None
            while S is None:
                h_ = _get_random_universal_hash_function(p, size)
                S = _construct_secondary_hash_table_no_collisions(mapped_keys[j], size, h_)
            T[j] = (h_, S)
    return T, h


def _construct_secondary_hash_table_no_collisions(keys, size, h_):
    S = Array.indexed(0, size - 1)
    for k in keys:
        if S[h_(k)] is not None:
            return None
        S[h_(k)] = k
    return S


def perfect_hashing_search(T, k, h):
    j = h(k)
    if T[j] is None:
        return None
    h_ = T[j][0]
    S = T[j][1]
    if S[h_(k)] == k:
        return j, h_(k)
    return None

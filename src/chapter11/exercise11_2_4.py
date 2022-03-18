from datastructures.hash_table import TakenPosition, FreePosition


def in_place_chained_hash_insert(T, x, h):
    hash = h(x.key)
    if not T[hash].taken:
        _allocate_hash_table_position(T, hash, x)
        T[hash].next = -1
    else:
        y = T[hash].element
        y_hash = h(y.key)
        y_new_position = T.free
        _allocate_hash_table_position(T, y_new_position, y)
        T[y_new_position].next = T[hash].next
        T[hash].element = x
        if y_hash == hash:
            T[hash].next = y_new_position
        else:
            while T[y_hash].next != hash:
                y_hash = T[y_hash].next
            T[y_hash].next = y_new_position
            T[hash].next = -1


def _allocate_hash_table_position(T, i, element):
    if T.free == -1:
        raise ValueError('overflow')
    position = T[i]
    if position.next != -1:
        T[position.next].prev = position.prev
    if position.prev != -1:
        T[position.prev].next = position.next
    if T.free == i:
        T.free = position.next
    T[i] = TakenPosition(element)


def in_place_chained_hash_delete(T, x, h):
    hash = h(x.key)
    if T[hash].element is x:
        if T[hash].next == -1:
            position_to_free = hash
        else:
            position_to_free = T[hash].next
            T[hash].element = T[position_to_free].element
            T[hash].next = T[position_to_free].next
    else:
        prev_position = hash
        curr_position = T[hash].next
        while T[curr_position].element is not x:
            prev_position = curr_position
            curr_position = T[curr_position].next
        T[prev_position].next = T[curr_position].next
        position_to_free = curr_position
    T[position_to_free] = FreePosition(-1, T.free)
    if T.free != -1:
        T[T.free].prev = position_to_free
    T.free = position_to_free


def in_place_chained_hash_search(T, k, h):
    hash = h(k)
    if not T[hash].taken:
        return None
    while hash != -1 and T[hash].element.key != k:
        hash = T[hash].next
    if hash != -1:
        return T[hash].element
    return None

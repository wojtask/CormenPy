def bit_vector_search(V, k):
    return k if V[k] == 1 else None


def bit_vector_insert(V, k):
    V[k] = 1


def bit_vector_delete(V, k):
    V[k] = 0

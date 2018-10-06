def table_insert(T, x):
    if T.size == 0:
        T.table = [None]
        T.size = 1
    if T.num == T.size:
        new_table = T.table + [None] * T.size
        T.table = new_table
        T.size = 2 * T.size
    T.table[T.num] = x
    T.num = T.num + 1

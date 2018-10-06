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


def table_delete(T, x):
    if T.num == T.size // 4:
        new_table = T.table[:T.size // 2]
        T.table = new_table
        T.size = T.size // 2
    T.table.remove(x)
    T.table.append(None)
    T.num = T.num - 1

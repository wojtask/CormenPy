def head_enqueue(D, x):
    if D.head == 1:
        D.head = D.length
    else:
        D.head = D.head - 1
    D[D.head] = x


def head_dequeue(D):
    x = D[D.head]
    if D.head == D.length:
        D.head = 1
    else:
        D.head = D.head + 1
    return x


def tail_enqueue(D, x):
    D[D.tail] = x
    if D.tail == D.length:
        D.tail = 1
    else:
        D.tail = D.tail + 1


def tail_dequeue(D):
    if D.tail == 1:
        D.tail = D.length
    else:
        D.tail = D.tail - 1
    return D[D.tail]

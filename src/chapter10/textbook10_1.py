def stack_empty(S):
    if S.top == 0:
        return True
    else:
        return False


def push(S, x):
    S.top += 1
    S[S.top] = x


def pop(S):
    if stack_empty(S):
        raise ValueError('underflow')
    else:
        S.top -= 1
        return S[S.top + 1]


def enqueue(Q, x):
    Q[Q.tail] = x
    if Q.tail == Q.length:
        Q.tail = 1
    else:
        Q.tail += 1


def dequeue(Q):
    x = Q[Q.head]
    if Q.head == Q.length:
        Q.head = 1
    else:
        Q.head += 1
    return x

from chapter10.textbook10_1 import enqueue, dequeue


def dequeue_(Q):
    if queue_empty(Q):
        raise ValueError('underflow')
    return dequeue(Q)


def queue_empty(Q):
    if Q.head == Q.tail:
        return True
    else:
        return False


def enqueue_(Q, x):
    if queue_full(Q):
        raise ValueError('overflow')
    enqueue(Q, x)


def queue_full(Q):
    if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length):
        return True
    else:
        return False

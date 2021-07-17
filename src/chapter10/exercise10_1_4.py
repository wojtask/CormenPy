from chapter10.textbook10_1 import enqueue, dequeue


def queue_empty(Q):
    if Q.head == Q.tail:
        return True
    else:
        return False


def enqueue_(Q, x):
    if Q.head == Q.tail + 1:
        raise ValueError('overflow')
    if Q.head == 1 and Q.tail == Q.length:
        raise ValueError('overflow')
    enqueue(Q, x)


def dequeue_(Q):
    if queue_empty(Q):
        raise ValueError('underflow')
    return dequeue(Q)

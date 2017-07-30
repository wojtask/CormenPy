from util import rbetween


def direct_address_maximum(T):
    m = T.length
    for i in rbetween(m - 1, 0):
        if T[i] is not None:
            return T[i]
    return None

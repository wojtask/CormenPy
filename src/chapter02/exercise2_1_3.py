def linear_search(A, v):
    i = 1
    while i <= A.length and A[i] != v:
        i += 1
    if i <= A.length:
        return i
    return None

def print_lcs_(c, X, Y, i, j):
    if i == 0 or j == 0:
        return
    if X[i] == Y[j]:
        print_lcs_(c, X, Y, i - 1, j - 1)
        print(X[i], end='')
    elif c[i, j] == c[i - 1, j]:
        print_lcs_(c, X, Y, i - 1, j)
    else:
        print_lcs_(c, X, Y, i, j - 1)

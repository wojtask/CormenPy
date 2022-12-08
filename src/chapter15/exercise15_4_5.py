from chapter15.textbook15_4 import lcs_length, print_lcs
from datastructures.array import Array


def lmis(X):
    n = X.length
    X_ = Array(X).sort()
    _, b = lcs_length(X, X_)
    print_lcs(b, X, n, n, end='\n')

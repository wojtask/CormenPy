import math


def two_arrays_median(X, pX, rX, Y, pY, rY):
    if rX - pX <= 1:
        return min(max(X[pX], Y[pY]), min(X[rX], Y[rY]))
    qX = math.floor((pX + rX) / 2)
    qX_ = math.ceil((pX + rX) / 2)
    qY = math.floor((pY + rY) / 2)
    qY_ = math.ceil((pY + rY) / 2)
    if X[qX] == Y[qY]:
        return X[qX]
    if X[qX] < Y[qY]:
        return two_arrays_median(X, qX, rX, Y, pY, qY_)
    else:
        return two_arrays_median(X, pX, qX_, Y, qY, rY)

import math


def joint_median(X, pX, rX, Y, pY, rY):
    if pX == rX:
        return min(X[pX], Y[pY])
    qX = math.floor((pX + rX) / 2)
    qX_ = math.ceil((pX + rX) / 2)
    qY = math.floor((pY + rY) / 2)
    qY_ = math.ceil((pY + rY) / 2)
    if X[qX] == Y[qY]:
        return X[qX]
    if X[qX] < Y[qY]:
        return joint_median(X, qX_, rX, Y, pY, qY)
    else:
        return joint_median(X, pX, qX, Y, qY_, rY)

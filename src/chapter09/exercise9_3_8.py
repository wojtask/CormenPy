from util import ceildiv


def joint_median(X, pX, rX, Y, pY, rY):
    if pX == rX:
        return min(X[pX], Y[pY])
    qX = (pX + rX) // 2
    qX_ = ceildiv(pX + rX, 2)
    qY = (pY + rY) // 2
    qY_ = ceildiv(pY + rY, 2)
    if X[qX] == Y[qY]:
        return X[qX]
    if X[qX] < Y[qY]:
        return joint_median(X, qX_, rX, Y, pY, qY)
    else:
        return joint_median(X, pX, qX, Y, qY_, rY)

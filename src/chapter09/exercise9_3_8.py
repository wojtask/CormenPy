def joint_median(X, pX, rX, Y, pY, rY):
    n = rX - pX + 1
    if n == 1:
        return min(X[pX], Y[pY])
    m = (n + 1) // 2
    if X[pX + m - 1] < Y[pY + m - 1]:
        return joint_median(X, rX - m + 1, rX, Y, pY, pY + m - 1)
    else:
        return joint_median(X, pX, pX + m - 1, Y, rY - m + 1, rY)

import math

from datastructures.interval import Interval
from util import between


def points_cover(points):
    points.sort()
    p = -math.inf
    I = set()
    for i in between(1, points.length):
        if points[i] - p > 1.0:
            p = points[i]
            I.add(Interval(p, p + 1))
    return I

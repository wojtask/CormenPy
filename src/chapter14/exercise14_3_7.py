from chapter14.exercise14_3_5 import interval_insert_exactly, interval_search_exactly
from chapter14.textbook14_3 import interval_search, interval_delete
from datastructures.array import Array
from datastructures.red_black_tree import RedBlackTree, IntervalNode


def rectangles_overlap(A):
    T = RedBlackTree(sentinel=IntervalNode(None, None))
    x_coordinates = Array((rectangle[0].low, rectangle) for rectangle in A) + \
        Array((rectangle[0].high, rectangle) for rectangle in A)
    x_coordinates.sort(key=lambda p: p[0])
    for p in x_coordinates:
        horizontal_side = p[1][0]
        vertical_side = p[1][1]
        if p[0] == horizontal_side.low:
            if interval_search(T, vertical_side) is not T.nil:
                return True
            interval_insert_exactly(T, IntervalNode(vertical_side.low, vertical_side))
        else:
            v = interval_search_exactly(T, vertical_side)
            interval_delete(T, v)
    return False

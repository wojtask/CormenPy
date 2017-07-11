from datastructures.red_black_tree import RedBlackTree


def right_rotate(T, x):
    # make sure the function works correctly for binary search trees and for red-black trees
    sentinel = T.nil if isinstance(T, RedBlackTree) else None

    y = x.left
    x.left = y.right
    if y.right is not sentinel:
        y.right.p = x
    y.p = x.p
    if x.p is sentinel:
        T.root = y
    else:
        if x == x.p.right:
            x.p.right = y
        else:
            x.p.left = y
    y.right = x
    x.p = y

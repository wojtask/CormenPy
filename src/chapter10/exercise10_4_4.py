def tree_walk(x):
    if x is not None:
        print(x.key)
        tree_walk(x.left_child)
        tree_walk(x.right_sibling)

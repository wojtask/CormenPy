def inorder_tree_walk(x):
    if x is not None:
        inorder_tree_walk(x.left)
        print(x.key)
        inorder_tree_walk(x.right)

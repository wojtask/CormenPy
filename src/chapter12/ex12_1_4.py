def preorder_tree_walk(x):
    if x is not None:
        print(x.key)
        preorder_tree_walk(x.left)
        preorder_tree_walk(x.right)


def postorder_tree_walk(x):
    if x is not None:
        postorder_tree_walk(x.left)
        postorder_tree_walk(x.right)
        print(x.key)

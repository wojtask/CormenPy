def stackless_inorder_visit(x):
    print(x.key)
    if x.right is not None:
        return x.right
    else:
        return x.p


def stackless_inorder_tree_walk(T):
    prev = None
    x = T.root
    while x is not None:
        if prev is x.p:
            if x.left is not None:
                next = x.left
            else:
                next = stackless_inorder_visit(x)
        elif prev is x.left:
            next = stackless_inorder_visit(x)
        else:
            next = x.p
        prev = x
        x = next

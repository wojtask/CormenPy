def stackless_inorder_visit(x):
    print(x.key)
    if x.right is not None:
        return x.right
    else:
        return x.p


def stackless_inorder_tree_walk(T):
    prev = None
    curr = T.root
    while curr is not None:
        if prev is curr.p:
            if curr.left is not None:
                next = curr.left
            else:
                next = stackless_inorder_visit(curr)
        elif prev is curr.left:
            next = stackless_inorder_visit(curr)
        else:
            next = curr.p
        prev = curr
        curr = next

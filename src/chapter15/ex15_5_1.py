def construct_optimal_bst(root):
    n = root.length
    print(optimal_bst_node(root, 1, n) + ' is the root')
    construct_optimal_bst_subtree(root, 1, n)


def construct_optimal_bst_subtree(root, i, j):
    if i <= j:
        print(optimal_bst_node(root, i, root[i, j] - 1) + ' is the left child of k' + str(root[i, j]))
        construct_optimal_bst_subtree(root, i, root[i, j] - 1)
        print(optimal_bst_node(root, root[i, j] + 1, j) + ' is the right child of k' + str(root[i, j]))
        construct_optimal_bst_subtree(root, root[i, j] + 1, j)


def optimal_bst_node(root, i, j):
    if i <= j:
        return 'k' + str(root[i, j])
    else:
        return 'd' + str(j)

import math
import random

from hamcrest import *

from array_util import get_random_array
from datastructures import binary_tree as bt, red_black_tree as rb
from datastructures.array import Array
from datastructures.binary_tree import BinaryTree
from datastructures.interval import Interval
from datastructures.red_black_tree import RedBlackTree, Color


def get_binary_tree_inorder_keys(tree):
    return get_binary_subtree_inorder_keys(tree.root, sentinel=getattr(tree, 'nil', None))


def get_binary_subtree_inorder_keys(node, sentinel):
    if node is sentinel:
        return Array()
    return get_binary_subtree_inorder_keys(node.left, sentinel) + [node.key] + get_binary_subtree_inorder_keys(
        node.right,
        sentinel)


def get_binary_tree_inorder_nodes(tree):
    return get_binary_subtree_inorder_nodes(tree.root, sentinel=getattr(tree, 'nil', None))


def get_binary_subtree_inorder_nodes(node, sentinel):
    if node is sentinel:
        return Array()
    return get_binary_subtree_inorder_nodes(node.left, sentinel) + [node] + get_binary_subtree_inorder_nodes(
        node.right,
        sentinel)


def get_random_binary_search_tree(min_size=1, max_size=20, max_value=999):
    tree_size = random.randint(min_size, max_size)
    inorder_keys = get_random_array(size=tree_size, min_value=0, max_value=max_value, unique=True).sort()
    inorder_nodes = Array(bt.Node(key) for key in inorder_keys)
    tree = BinaryTree()
    tree.root = get_random_binary_search_subtree(inorder_nodes)
    return tree, inorder_nodes, inorder_keys


def get_random_binary_search_subtree(inorder_nodes):
    if not inorder_nodes:
        return None
    i = random.randint(1, inorder_nodes.length)
    node = inorder_nodes[i]
    left_node = get_random_binary_search_subtree(inorder_nodes[:i - 1])
    if left_node is not None:
        node.left = left_node
        left_node.p = node
    right_node = get_random_binary_search_subtree(inorder_nodes[i + 1:])
    if right_node is not None:
        node.right = right_node
        right_node.p = node
    return node


def assert_parent_pointers_consistent(tree):
    sentinel = getattr(tree, 'nil', None)
    if tree.root is not sentinel:
        assert_that(tree.root.p, is_(sentinel))
        assert_subtree_parent_pointers_consistent(tree.root, sentinel)


def assert_subtree_parent_pointers_consistent(node, sentinel):
    if node.left is not sentinel:
        assert_that(node.left.p, is_(node))
        assert_subtree_parent_pointers_consistent(node.left, sentinel)
    if node.right is not sentinel:
        assert_that(node.right.p, is_(node))
        assert_subtree_parent_pointers_consistent(node.right, sentinel)


def assert_binary_search_tree(tree):
    sentinel = getattr(tree, 'nil', None)
    if tree.root is not sentinel:
        assert_binary_search_subtree(tree.root, sentinel)


def assert_binary_search_subtree(node, sentinel):
    if node.left is not sentinel:
        left_keys = get_binary_subtree_inorder_keys(node.left, sentinel)
        for left_key in left_keys:
            assert_that(left_key, is_(less_than_or_equal_to(node.key)))
        assert_binary_search_subtree(node.left, sentinel)
    if node.right is not sentinel:
        right_keys = get_binary_subtree_inorder_keys(node.right, sentinel)
        for right_key in right_keys:
            assert_that(right_key, is_(greater_than_or_equal_to(node.key)))
        assert_binary_search_subtree(node.right, sentinel)


def get_random_red_black_tree(black_height=3, min_value=0, max_value=999, sentinel=rb.Node(None)):
    nodes = Array()
    tree = RedBlackTree(get_random_red_black_subtree(black_height, nodes), sentinel)
    tree_size = nodes.length
    inorder_keys = get_random_array(size=tree_size, min_value=min_value, max_value=max_value, unique=True).sort()
    fill_subtree_with_keys(tree.root, inorder_keys, sentinel=tree.nil)
    inorder_nodes = nodes.sort(key=lambda node: node.key)
    return tree, inorder_nodes, inorder_keys


def get_random_red_black_subtree(black_height, nodes):
    if black_height == 0:
        return None

    # at each level of the tree we try to create an extra red node in the left subtree
    if random.choice(list(Color)) == Color.RED:
        left_subtree_root = create_red_node_in_subtree(black_height, nodes)
    else:
        left_subtree_root = get_random_red_black_subtree(black_height - 1, nodes)

    # ...and we repeat the same for the right subtree
    if random.choice(list(Color)) == Color.RED:
        right_subtree_root = create_red_node_in_subtree(black_height, nodes)
    else:
        right_subtree_root = get_random_red_black_subtree(black_height - 1, nodes)

    root = rb.Node(None, left=left_subtree_root, right=right_subtree_root)
    nodes.append(root)
    return root


def create_red_node_in_subtree(black_height, nodes):
    left_subtree_root = get_random_red_black_subtree(black_height - 1, nodes)
    right_subtree_root = get_random_red_black_subtree(black_height - 1, nodes)
    subtree_root = rb.Node(None, left=left_subtree_root, right=right_subtree_root, color=Color.RED)
    nodes.append(subtree_root)
    return subtree_root


def fill_subtree_with_keys(node, inorder_keys, sentinel):
    if node is sentinel:
        return
    left_subtree_size = get_subtree_size(node.left, sentinel)
    node.key = inorder_keys[left_subtree_size + 1]
    fill_subtree_with_keys(node.left, inorder_keys[:left_subtree_size], sentinel)
    fill_subtree_with_keys(node.right, inorder_keys[left_subtree_size + 2:], sentinel)


def get_subtree_size(node, sentinel):
    if node is sentinel:
        return 0
    return 1 + get_subtree_size(node.left, sentinel) + get_subtree_size(node.right, sentinel)


def assert_red_black_tree(tree):
    sentinel = getattr(tree, 'nil', None)
    if tree.root is not None:
        assert_that(tree.root.color, is_(Color.BLACK))
    if sentinel is not None:
        assert_that(tree.nil.color, is_(Color.BLACK))
    if tree.root is not sentinel:
        assert_binary_search_tree(tree)
        assert_red_black_property_4(tree.root, sentinel)
        assert_red_black_property_5(tree.root, sentinel)


def assert_red_black_property_4(node, sentinel):
    if node.color == Color.RED:
        if node.left is not sentinel:
            assert_that(node.left.color, is_(Color.BLACK))
        if node.right is not sentinel:
            assert_that(node.right.color, is_(Color.BLACK))
    if node.left is not sentinel:
        assert_red_black_property_4(node.left, sentinel)
    if node.right is not sentinel:
        assert_red_black_property_4(node.right, sentinel)


def assert_red_black_property_5(node, sentinel):
    left_bh = right_bh = 0
    if node.left is not sentinel:
        left_bh = assert_red_black_property_5(node.left, sentinel)
        if node.left.color == Color.BLACK:
            left_bh += 1
    if node.right is not sentinel:
        right_bh = assert_red_black_property_5(node.right, sentinel)
        if node.right.color == Color.BLACK:
            right_bh += 1
    assert_that(left_bh, is_(equal_to(right_bh)))
    return left_bh


def assert_avl_tree(tree):
    assert_binary_search_tree(tree)
    assert_avl_subtree(tree.root)


def assert_avl_subtree(node):
    if node is None:
        return -1
    hl = assert_avl_subtree(node.left)
    hr = assert_avl_subtree(node.right)
    assert_that(node.h, is_(equal_to(max(hl, hr) + 1)))
    assert_that(abs(hr - hl), is_(less_than_or_equal_to(1)))
    return node.h


def assert_treap(tree):
    assert_binary_search_tree(tree)
    if tree.root is not None:
        assert_subtreap(tree.root)


def assert_subtreap(node):
    if node.left is not None:
        assert_that(node.priority, is_(less_than(node.left.priority)))
        assert_subtreap(node.left)
    if node.right is not None:
        assert_that(node.priority, is_(less_than(node.right.priority)))
        assert_subtreap(node.right)


def get_random_os_tree(black_height=3, max_value=999):
    tree, inorder_nodes, inorder_keys = get_random_red_black_tree(black_height, max_value=max_value,
                                                                  sentinel=rb.OSNode(None))
    augment_to_os_tree(tree)
    return tree, inorder_nodes, inorder_keys


def augment_to_os_tree(tree):
    tree.nil.size = 0
    if tree.root is not tree.nil:
        augment_to_os_subtree(tree.root, tree.nil)


def augment_to_os_subtree(node, sentinel):
    left_size = right_size = 0
    if node.left is not sentinel:
        left_size = augment_to_os_subtree(node.left, sentinel)
    if node.right is not sentinel:
        right_size = augment_to_os_subtree(node.right, sentinel)
    node.size = left_size + right_size + 1
    return node.size


def assert_os_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_os_subtree(tree.root, tree.nil)


def assert_os_subtree(node, sentinel):
    assert_that(node.size, is_(equal_to(node.left.size + node.right.size + 1)))
    if node.left is not sentinel:
        assert_os_subtree(node.left, sentinel)
    if node.right is not sentinel:
        assert_os_subtree(node.right, sentinel)


def get_random_interval_tree(black_height=3, max_value=999):
    # we treat max_value as the upper bound for high endpoints
    # the procedure is generating intervals at most (.1 * max_value) units wide
    tree, inorder_nodes, inorder_keys = get_random_red_black_tree(black_height, max_value=int(.9 * max_value),
                                                                  sentinel=rb.IntervalNode(None, None))
    # we will allow keys and intervals to be non unique
    tree_size = inorder_nodes.length
    inorder_keys = get_random_array(size=tree_size, max_value=max_value).sort()
    fill_subtree_with_intervals(tree.root, inorder_keys, max_value, sentinel=tree.nil)
    augment_to_interval_tree(tree)
    return tree, inorder_nodes, inorder_keys


def fill_subtree_with_intervals(node, inorder_keys, max_value, sentinel):
    if node is sentinel:
        return
    left_subtree_size = get_subtree_size(node.left, sentinel)
    node.key = inorder_keys[left_subtree_size + 1]
    high_endpoint = random.randint(node.key, node.key + int(.1 * max_value))
    node.int = Interval(node.key, high_endpoint)
    fill_subtree_with_intervals(node.left, inorder_keys[:left_subtree_size], max_value, sentinel)
    fill_subtree_with_intervals(node.right, inorder_keys[left_subtree_size + 2:], max_value, sentinel)


def augment_to_interval_tree(tree):
    tree.nil.max = -math.inf
    if tree.root is not tree.nil:
        augment_to_interval_subtree(tree.root, tree.nil)


def augment_to_interval_subtree(node, sentinel):
    max_left = max_right = -math.inf
    if node.left is not sentinel:
        max_left = augment_to_interval_subtree(node.left, sentinel)
    if node.right is not sentinel:
        max_right = augment_to_interval_subtree(node.right, sentinel)
    node.max = max(node.int.high, max_left, max_right)
    return node.max


def assert_interval_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_interval_subtree(tree.root, tree.nil)


def assert_interval_subtree(node, sentinel):
    assert_that(node.key, is_(equal_to(node.int.low)))
    assert_that(node.max, is_(equal_to(max(node.int.high, node.left.max, node.right.max))))
    if node.left is not sentinel:
        assert_interval_subtree(node.left, sentinel)
    if node.right is not sentinel:
        assert_interval_subtree(node.right, sentinel)


def assert_interval_pom_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_interval_pom_subtree(tree.root, tree.nil)


def assert_interval_pom_subtree(node, sentinel):
    assert_that(node.sum, is_(equal_to(node.left.sum + (node.low - node.high) + node.right.sum)))
    assert_that(node.max, is_(equal_to(max(node.left.max,
                                           node.left.sum + node.low,
                                           node.left.sum + (node.low - node.high) + node.right.max))))
    if node.max == node.left.max:
        assert_that(node.pom, is_(equal_to(node.left.pom)))
    elif node.max == node.left.sum + node.low:
        assert_that(node.pom, is_(equal_to(node.key)))
    else:
        assert_that(node.pom, is_(equal_to(node.right.pom)))
    if node.left is not sentinel:
        assert_interval_pom_subtree(node.left, sentinel)
    if node.right is not sentinel:
        assert_interval_pom_subtree(node.right, sentinel)

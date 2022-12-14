import math
import random

from hamcrest import *

from array_util import get_random_array
from datastructures import binary_tree as bt, red_black_tree as rb
from datastructures.array import Array
from datastructures.binary_tree import BinaryTree
from datastructures.essential import Interval
from datastructures.red_black_tree import RedBlackTree, Color, JoinableRedBlackTree


def get_binary_search_tree_inorder_keys(tree):
    return get_binary_search_subtree_inorder_keys(tree.root, sentinel=getattr(tree, 'nil', None))


def get_binary_search_subtree_inorder_keys(subtree_root, sentinel):
    if subtree_root is sentinel:
        return Array()
    return get_binary_search_subtree_inorder_keys(subtree_root.left, sentinel) \
        + Array.of(subtree_root.key) \
        + get_binary_search_subtree_inorder_keys(subtree_root.right, sentinel)


def get_binary_search_tree_inorder_nodes(tree):
    return get_binary_search_subtree_inorder_nodes(tree.root, sentinel=getattr(tree, 'nil', None))


def get_binary_search_subtree_inorder_nodes(subtree_root, sentinel):
    if subtree_root is sentinel:
        return Array()
    return get_binary_search_subtree_inorder_nodes(subtree_root.left, sentinel) \
        + Array.of(subtree_root) \
        + get_binary_search_subtree_inorder_nodes(subtree_root.right, sentinel)


def get_random_binary_search_tree(min_size=1, max_size=20, max_value=999, node_ctor=bt.Node):
    tree_size = random.randint(min_size, max_size)
    inorder_keys = get_random_array(size=tree_size, min_value=0, max_value=max_value, unique=True).sort()
    inorder_nodes = Array(node_ctor(key) for key in inorder_keys)
    return BinaryTree(get_random_binary_search_subtree(inorder_nodes))


def get_random_binary_search_subtree(inorder_nodes):
    if not inorder_nodes:
        return None
    i = random.randint(1, inorder_nodes.length)
    subtree_root = inorder_nodes[i]
    left_subtree_root = get_random_binary_search_subtree(inorder_nodes[:i - 1])
    if left_subtree_root is not None:
        subtree_root.left = left_subtree_root
        left_subtree_root.p = subtree_root
    right_subtree_root = get_random_binary_search_subtree(inorder_nodes[i + 1:])
    if right_subtree_root is not None:
        subtree_root.right = right_subtree_root
        right_subtree_root.p = subtree_root
    return subtree_root


def assert_parent_pointers_consistent(tree):
    sentinel = getattr(tree, 'nil', None)
    if tree.root is not sentinel:
        assert_that(tree.root.p, is_(sentinel))
        assert_subtree_parent_pointers_consistent(tree.root, sentinel)


def assert_subtree_parent_pointers_consistent(subtree_root, sentinel):
    if subtree_root.left is not sentinel:
        assert_that(subtree_root.left.p, is_(subtree_root))
        assert_subtree_parent_pointers_consistent(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        assert_that(subtree_root.right.p, is_(subtree_root))
        assert_subtree_parent_pointers_consistent(subtree_root.right, sentinel)


def assert_binary_search_tree(tree):
    sentinel = getattr(tree, 'nil', None)
    if tree.root is not sentinel:
        assert_binary_search_subtree(tree.root, sentinel)


def assert_binary_search_subtree(subtree_root, sentinel):
    if subtree_root.left is not sentinel:
        left_subtree_keys = get_binary_search_subtree_inorder_keys(subtree_root.left, sentinel)
        for key in left_subtree_keys:
            assert_that(key, is_(less_than_or_equal_to(subtree_root.key)))
        assert_binary_search_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        right_subtree_keys = get_binary_search_subtree_inorder_keys(subtree_root.right, sentinel)
        for key in right_subtree_keys:
            assert_that(key, is_(greater_than_or_equal_to(subtree_root.key)))
        assert_binary_search_subtree(subtree_root.right, sentinel)


def get_random_red_black_tree(black_height=3, min_value=0, max_value=999, node_ctor=rb.Node, with_sentinel=True):
    nodes = Array()
    sentinel = node_ctor(None) if with_sentinel else None
    tree = RedBlackTree(get_random_red_black_subtree_with_black_root(black_height, nodes, node_ctor, sentinel),
                        sentinel)
    tree_size = nodes.length
    inorder_keys = get_random_array(size=tree_size, min_value=min_value, max_value=max_value, unique=True).sort()
    fill_subtree_with_keys(tree.root, inorder_keys, sentinel=tree.nil)
    return tree


def get_random_red_black_subtree_with_black_root(black_height, nodes, node_ctor, sentinel):
    if black_height == 0:
        return sentinel

    if random.choice(list(Color)) == Color.RED:
        left_subtree_root = get_random_red_black_subtree_with_red_root(black_height, nodes, node_ctor, sentinel)
    else:
        left_subtree_root = get_random_red_black_subtree_with_black_root(black_height - 1, nodes, node_ctor, sentinel)

    if random.choice(list(Color)) == Color.RED:
        right_subtree_root = get_random_red_black_subtree_with_red_root(black_height, nodes, node_ctor, sentinel)
    else:
        right_subtree_root = get_random_red_black_subtree_with_black_root(black_height - 1, nodes, node_ctor, sentinel)

    subtree_root = node_ctor(None, left=left_subtree_root, right=right_subtree_root, color=Color.BLACK)
    nodes.append(subtree_root)
    return subtree_root


def get_random_red_black_subtree_with_red_root(black_height, nodes, node_ctor, sentinel):
    left_subtree_root = get_random_red_black_subtree_with_black_root(black_height - 1, nodes, node_ctor, sentinel)
    right_subtree_root = get_random_red_black_subtree_with_black_root(black_height - 1, nodes, node_ctor, sentinel)
    subtree_root = node_ctor(None, left=left_subtree_root, right=right_subtree_root, color=Color.RED)
    nodes.append(subtree_root)
    return subtree_root


def fill_subtree_with_keys(subtree_root, inorder_keys, sentinel):
    if subtree_root is sentinel:
        return
    left_subtree_size = get_subtree_size(subtree_root.left, sentinel)
    subtree_root.key = inorder_keys[left_subtree_size + 1]
    fill_subtree_with_keys(subtree_root.left, inorder_keys[:left_subtree_size], sentinel)
    fill_subtree_with_keys(subtree_root.right, inorder_keys[left_subtree_size + 2:], sentinel)


def get_subtree_size(subtree_root, sentinel):
    if subtree_root is sentinel:
        return 0
    return get_subtree_size(subtree_root.left, sentinel) + get_subtree_size(subtree_root.right, sentinel) + 1


def assert_red_black_tree(tree):
    sentinel = getattr(tree, 'nil', None)
    if tree.root is not None:
        assert_that(tree.root.color, is_(Color.BLACK))
    if sentinel is not None:
        assert_that(sentinel.color, is_(Color.BLACK))
    if tree.root is not sentinel:
        assert_binary_search_tree(tree)
        assert_red_black_property_4(tree.root, sentinel)
        assert_red_black_property_5(tree.root, sentinel)


def assert_red_black_property_4(subtree_root, sentinel):
    if subtree_root.color == Color.RED:
        if subtree_root.left is not sentinel:
            assert_that(subtree_root.left.color, is_(Color.BLACK))
        if subtree_root.right is not sentinel:
            assert_that(subtree_root.right.color, is_(Color.BLACK))
    if subtree_root.left is not sentinel:
        assert_red_black_property_4(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        assert_red_black_property_4(subtree_root.right, sentinel)


def assert_red_black_property_5(subtree_root, sentinel):
    left_bh = right_bh = 0
    if subtree_root.left is not sentinel:
        left_bh = assert_red_black_property_5(subtree_root.left, sentinel)
        if subtree_root.left.color == Color.BLACK:
            left_bh += 1
    if subtree_root.right is not sentinel:
        right_bh = assert_red_black_property_5(subtree_root.right, sentinel)
        if subtree_root.right.color == Color.BLACK:
            right_bh += 1
    assert_that(left_bh, is_(equal_to(right_bh)))
    return left_bh


def get_random_joinable_red_black_tree(black_height=3, min_value=0, max_value=999):
    nodes = Array()
    tree = JoinableRedBlackTree(get_random_red_black_subtree_with_black_root(black_height, nodes, rb.Node, None),
                                bh=black_height)
    tree_size = nodes.length
    inorder_keys = get_random_array(size=tree_size, min_value=min_value, max_value=max_value, unique=True).sort()
    fill_subtree_with_keys(tree.root, inorder_keys, None)
    return tree


def assert_avl_tree(tree):
    assert_binary_search_tree(tree)
    assert_avl_subtree(tree.root)


def assert_avl_subtree(subtree_root):
    if subtree_root is None:
        return -1
    hl = assert_avl_subtree(subtree_root.left)
    hr = assert_avl_subtree(subtree_root.right)
    assert_that(subtree_root.h, is_(equal_to(max(hl, hr) + 1)))
    assert_that(abs(hr - hl), is_(less_than_or_equal_to(1)))
    return subtree_root.h


def assert_treap(tree):
    assert_binary_search_tree(tree)
    if tree.root is not None:
        assert_subtreap(tree.root)


def assert_subtreap(subtree_root):
    if subtree_root.left is not None:
        assert_that(subtree_root.priority, is_(less_than(subtree_root.left.priority)))
        assert_subtreap(subtree_root.left)
    if subtree_root.right is not None:
        assert_that(subtree_root.priority, is_(less_than(subtree_root.right.priority)))
        assert_subtreap(subtree_root.right)


def get_random_os_tree(black_height=3, max_value=999):
    tree = get_random_red_black_tree(black_height, max_value=max_value, node_ctor=rb.OSNode)
    augment_to_os_tree(tree)
    return tree


def augment_to_os_tree(tree):
    tree.nil.size = 0
    if tree.root is not tree.nil:
        augment_to_os_subtree(tree.root, tree.nil)


def augment_to_os_subtree(subtree_root, sentinel):
    left_size = right_size = 0
    if subtree_root.left is not sentinel:
        left_size = augment_to_os_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        right_size = augment_to_os_subtree(subtree_root.right, sentinel)
    subtree_root.size = left_size + right_size + 1
    return subtree_root.size


def assert_os_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_os_subtree(tree.root, tree.nil)


def assert_os_subtree(subtree_root, sentinel):
    assert_that(subtree_root.size, is_(equal_to(subtree_root.left.size + subtree_root.right.size + 1)))
    if subtree_root.left is not sentinel:
        assert_os_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        assert_os_subtree(subtree_root.right, sentinel)


def get_random_ranked_os_tree(black_height=3, max_value=999):
    tree = get_random_red_black_tree(black_height, max_value=max_value, node_ctor=rb.RankedOSNode)
    augment_to_ranked_os_tree(tree)
    return tree


def augment_to_ranked_os_tree(tree):
    if tree.root is not tree.nil:
        augment_to_ranked_os_subtree(tree.root, tree.nil)


def augment_to_ranked_os_subtree(subtree_root, sentinel):
    left_size = right_size = 0
    if subtree_root.left is not sentinel:
        left_size = augment_to_ranked_os_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        right_size = augment_to_ranked_os_subtree(subtree_root.right, sentinel)
    subtree_root.rank = left_size + 1
    return left_size + right_size + 1


def assert_ranked_os_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_ranked_os_subtree(tree.root, tree.nil)


def assert_ranked_os_subtree(subtree_root, sentinel):
    left_size = right_size = 0
    if subtree_root.left is not sentinel:
        left_size = assert_ranked_os_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        right_size = assert_ranked_os_subtree(subtree_root.right, sentinel)
    assert_that(subtree_root.rank, is_(equal_to(left_size + 1)))
    return left_size + right_size + 1


def get_random_interval_tree(black_height=3, max_value=999):
    # max_value is treated as the upper bound for high endpoints
    # the procedure generates intervals of lengths at most (.1 * max_value)
    tree = get_random_red_black_tree(black_height, max_value=int(.9 * max_value), node_ctor=rb.IntervalNode)
    inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
    tree_size = inorder_nodes.length
    # overwrite the previous keys, allow to non-unique keys and intervals
    inorder_keys = get_random_array(size=tree_size, max_value=max_value).sort()
    fill_subtree_with_intervals(tree.root, inorder_keys, max_value, sentinel=tree.nil)
    augment_to_interval_tree(tree)
    return tree


def fill_subtree_with_intervals(subtree_root, inorder_keys, max_value, sentinel):
    if subtree_root is sentinel:
        return
    left_subtree_size = get_subtree_size(subtree_root.left, sentinel)
    subtree_root.key = inorder_keys[left_subtree_size + 1]
    high_endpoint = random.randint(subtree_root.key, subtree_root.key + int(.1 * max_value))
    subtree_root.int = Interval(subtree_root.key, high_endpoint)
    fill_subtree_with_intervals(subtree_root.left, inorder_keys[:left_subtree_size], max_value, sentinel)
    fill_subtree_with_intervals(subtree_root.right, inorder_keys[left_subtree_size + 2:], max_value, sentinel)


def augment_to_interval_tree(tree):
    tree.nil.max = -math.inf
    if tree.root is not tree.nil:
        augment_to_interval_subtree(tree.root, tree.nil)


def augment_to_interval_subtree(subtree_root, sentinel):
    max_left = max_right = -math.inf
    if subtree_root.left is not sentinel:
        max_left = augment_to_interval_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        max_right = augment_to_interval_subtree(subtree_root.right, sentinel)
    subtree_root.max = max(subtree_root.int.high, max_left, max_right)
    return subtree_root.max


def assert_interval_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_interval_subtree(tree.root, tree.nil)


def assert_interval_subtree(subtree_root, sentinel):
    assert_that(subtree_root.key, is_(equal_to(subtree_root.int.low)))
    assert_that(subtree_root.max,
                is_(equal_to(max(subtree_root.int.high, subtree_root.left.max, subtree_root.right.max))))
    if subtree_root.left is not sentinel:
        assert_interval_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        assert_interval_subtree(subtree_root.right, sentinel)


def assert_interval_pom_tree(tree):
    assert_red_black_tree(tree)
    assert_parent_pointers_consistent(tree)
    if tree.root is not tree.nil:
        assert_interval_pom_subtree(tree.root, tree.nil)


def assert_interval_pom_subtree(subtree_root, sentinel):
    assert_that(subtree_root.sum,
                is_(equal_to(subtree_root.left.sum + (subtree_root.low - subtree_root.high) + subtree_root.right.sum)))
    assert_that(subtree_root.max, is_(equal_to(max(subtree_root.left.max,
                                                   subtree_root.left.sum + subtree_root.low,
                                                   subtree_root.left.sum +
                                                   (subtree_root.low - subtree_root.high) +
                                                   subtree_root.right.max))))
    if subtree_root.max == subtree_root.left.max:
        assert_that(subtree_root.pom, is_(equal_to(subtree_root.left.pom)))
    elif subtree_root.max == subtree_root.left.sum + subtree_root.low:
        assert_that(subtree_root.pom, is_(equal_to(subtree_root.key)))
    else:
        assert_that(subtree_root.pom, is_(equal_to(subtree_root.right.pom)))
    if subtree_root.left is not sentinel:
        assert_interval_pom_subtree(subtree_root.left, sentinel)
    if subtree_root.right is not sentinel:
        assert_interval_pom_subtree(subtree_root.right, sentinel)

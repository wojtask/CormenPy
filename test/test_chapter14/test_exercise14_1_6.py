from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter14.exercise14_1_6 import ranked_os_insert, ranked_os_delete
from datastructures.red_black_tree import RedBlackTree, RankedOSNode
from tree_util import get_binary_search_tree_inorder_keys, get_binary_search_tree_inorder_nodes, \
    assert_ranked_os_tree, get_random_ranked_os_tree


class TestExercise14_1_6(TestCase):

    def test_ranked_os_insert(self):
        keys = get_random_array(size=20)
        tree = RedBlackTree(sentinel=RankedOSNode(None))

        for i, key in enumerate(keys, start=1):
            ranked_os_insert(tree, RankedOSNode(key))

            assert_ranked_os_tree(tree)

        actual_keys = get_binary_search_tree_inorder_keys(tree)
        assert_that(actual_keys, contains_inanyorder(*keys))

    def test_ranked_os_delete(self):
        tree = get_random_ranked_os_tree(black_height=3)
        inorder_nodes = get_binary_search_tree_inorder_nodes(tree)
        inorder_keys = get_binary_search_tree_inorder_keys(tree)

        while inorder_nodes:
            node = inorder_nodes.random_choice()
            inorder_keys.remove(node.key)

            ranked_os_delete(tree, node)

            assert_ranked_os_tree(tree)
            actual_keys = get_binary_search_tree_inorder_keys(tree)
            assert_that(actual_keys, contains_inanyorder(*inorder_keys))
            inorder_nodes = get_binary_search_tree_inorder_nodes(tree)

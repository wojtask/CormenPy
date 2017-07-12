import random
from unittest import TestCase

from chapter13.textbook import left_rotate, rb_insert, rb_delete
from datastructures.red_black_tree import RedBlackTree, Node
from test.test_datastructures.tree_util import binary_tree_to_list, assert_red_black_tree, assert_binary_search_tree, \
    assert_parent_pointers_consistent


class Chapter13Test(TestCase):
    def setUp(self):
        random.seed()

    def test_left_rotate_binary_tree(self):
        from datastructures.binary_tree import BinaryTree, Node
        alpha, beta, gamma = Node(1), Node(3), Node(5)
        y = Node(4, left=beta, right=gamma)
        x = Node(2, left=alpha, right=y)
        z = Node(100, left=x)
        tree = BinaryTree(z)
        left_rotate(tree, x)
        self.assertIs(z.left, y)
        self.assertIs(y.left, x)
        self.assertIs(x.left, alpha)
        self.assertIs(x.right, beta)
        self.assertIs(y.right, gamma)
        assert_binary_search_tree(tree)
        assert_parent_pointers_consistent(tree)

    def test_left_rotate_red_black_tree(self):
        alpha, beta, gamma = Node(1), Node(3), Node(5)
        y = Node(4, left=beta, right=gamma)
        x = Node(2, left=alpha, right=y)
        z = Node(100, left=x)
        tree = RedBlackTree(z)
        left_rotate(tree, x)
        self.assertIs(z.left, y)
        self.assertIs(y.left, x)
        self.assertIs(x.left, alpha)
        self.assertIs(x.right, beta)
        self.assertIs(y.right, gamma)
        assert_binary_search_tree(tree, sentinel=tree.nil)
        assert_parent_pointers_consistent(tree, sentinel=tree.nil)

    def test_rb_insert(self):
        tree_size = 20
        tree = RedBlackTree()
        keys = [random.randrange(1000) for _ in range(tree_size)]
        for i in range(tree_size):
            rb_insert(tree, Node(keys[i]))
            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
        actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
        self.assertEqual(sorted(actual_keys), sorted(keys))

    def test_rb_delete(self):
        # first we build a red-black tree using rb_insert
        tree_size = 20
        tree = RedBlackTree()
        keys = [random.randrange(1000) for _ in range(tree_size)]
        nodes = [Node(key) for key in keys]
        for i in range(tree_size):
            rb_insert(tree, nodes[i])

        # then we are removing nodes from the tree in random order
        random.shuffle(nodes)
        for i in range(tree_size):
            y = rb_delete(tree, nodes[i])
            if y != nodes[i]:
                # this means that rb_delete actually removed the node's successor so we need to swap them in nodes list
                j = nodes.index(y)
                nodes[i], nodes[j] = nodes[j], nodes[i]
            assert_red_black_tree(tree)
            assert_parent_pointers_consistent(tree, sentinel=tree.nil)
            actual_keys = binary_tree_to_list(tree, sentinel=tree.nil)
            self.assertEqual(len(actual_keys), tree_size - i - 1)
            self.assertTrue(all(x in keys for x in actual_keys))

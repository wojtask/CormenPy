import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter15.textbook15_5 import optimal_bst
from util import between


def get_probabilities_for_optimal_bst():
    n = random.randint(1, 10)
    p = get_random_array(size=n)
    q = get_random_array(size=n + 1, start=0)
    total = sum(p + q)
    for i in between(1, n):
        p[i] /= total
    for i in between(0, n):
        q[i] /= total
    return p.save_state(), q.save_state()


def assert_root_array_consistent(root):
    n = root.length
    for i in between(1, n):
        for j in between(i, n):
            assert_that(root[i, j], is_(greater_than_or_equal_to(i)))
            assert_that(root[i, j], is_(less_than_or_equal_to(j)))


def get_bst_cost(root, p, q):
    return get_bst_subtree_cost(root, p, q, 0, 1, p.length)


def get_bst_subtree_cost(root, p, q, d, i, j):
    if i > j:
        return (d + 1) * q[j]
    return (d + 1) * p[root[i, j]] + \
        get_bst_subtree_cost(root, p, q, d + 1, i, root[i, j] - 1) + \
        get_bst_subtree_cost(root, p, q, d + 1, root[i, j] + 1, j)


def get_minimum_bst_cost_bruteforce(p, q):
    return get_minimum_subtree_cost_bruteforce(p, q, 1, p.length, 0)


def get_minimum_subtree_cost_bruteforce(p, q, i, j, d):
    if i > j:
        return (d + 1) * q[j]
    min_cost = math.inf
    for k in between(i, j):
        cost = (d + 1) * p[k] + \
               get_minimum_subtree_cost_bruteforce(p, q, i, k - 1, d + 1) + \
               get_minimum_subtree_cost_bruteforce(p, q, k + 1, j, d + 1)
        min_cost = min(min_cost, cost)
    return min_cost


class TestTextbook15_5(TestCase):

    def test_optimal_bst(self):
        p, q = get_probabilities_for_optimal_bst()

        e, root = optimal_bst(p, q, p.length)

        assert_root_array_consistent(root)
        expected_minimum_cost = get_minimum_bst_cost_bruteforce(p, q)
        actual_minimum_cost = get_bst_cost(root, p, q)
        assert_that(actual_minimum_cost, expected_minimum_cost)

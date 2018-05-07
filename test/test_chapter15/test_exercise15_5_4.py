from unittest import TestCase

from hamcrest import *

from chapter15.exercise15_5_4 import effective_optimal_bst
from test_chapter15.test_textbook15_5 import get_probabilities_for_optimal_bst, assert_root_array_consistent, \
    get_minimum_bst_cost_bruteforce, get_bst_cost


class TestExercise15_5_4(TestCase):

    def test_effective_optimal_bst(self):
        p, q = get_probabilities_for_optimal_bst()

        e, root = effective_optimal_bst(p, q, p.length)

        assert_root_array_consistent(root)
        expected_minimum_cost = get_minimum_bst_cost_bruteforce(p, q)
        actual_minimum_cost = get_bst_cost(root, p, q)
        assert_that(actual_minimum_cost, is_(equal_to(expected_minimum_cost)))

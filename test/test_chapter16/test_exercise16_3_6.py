import itertools
import math
import random
import string
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter16.exercise16_3_6 import ternary_huffman
from datastructures.array import Array
from util import between


def all_ternary_trees(s, d=0):
    if s.length == 1:
        yield s[1] * d
    elif s.length == 2:
        yield (s[1] + s[2]) * (d + 1)
    elif s.length == 3:
        yield (s[1] + s[2] + s[3]) * (d + 1)
    else:
        for i in between(2, s.length - 1):
            for j in between(i, s.length):
                for lb in all_ternary_trees(s[:i - 1], d + 1):
                    for mb in all_ternary_trees(s[i:j], d + 1):
                        for rb in all_ternary_trees(s[j + 1:], d + 1):
                            yield lb + mb + rb


def compute_tree_cost(node, d=0):
    if node is None:
        return 0
    if node.left is None and node.middle is None and node.right is None:
        return node.f * d
    return compute_tree_cost(node.left, d + 1) + \
        compute_tree_cost(node.middle, d + 1) + \
        compute_tree_cost(node.right, d + 1)


class TestExercise16_3_6(TestCase):

    def test_ternary_huffman(self):
        n = random.randint(1, 6)
        characters = string.ascii_lowercase[:n]
        frequencies = get_random_array(size=n)
        char_freq = set(zip(characters, frequencies))

        actual_root = ternary_huffman(char_freq)

        actual_tree_cost = compute_tree_cost(actual_root)
        expected_tree_cost = math.inf
        for reordering in itertools.permutations(frequencies):
            for cost in all_ternary_trees(Array(reordering)):
                expected_tree_cost = min(expected_tree_cost, cost)
        assert_that(actual_tree_cost, is_(equal_to(expected_tree_cost)))

import io
import random
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from chapter14.exercise14_2_5 import rb_enumerate
from tree_util import get_random_red_black_tree


class TestExercise14_2_5(TestCase):

    def test_rb_enumerate(self):
        tree, nodes, _ = get_random_red_black_tree()
        lower_bound = random.randint(0, 999)
        upper_bound = random.randint(0, 999)
        if lower_bound > upper_bound:
            lower_bound, upper_bound = upper_bound, lower_bound

        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            rb_enumerate(tree, tree.root, lower_bound, upper_bound)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        for x in actual_output:
            assert_that(x, is_(greater_than_or_equal_to(lower_bound)))
            assert_that(x, is_(less_than_or_equal_to(upper_bound)))

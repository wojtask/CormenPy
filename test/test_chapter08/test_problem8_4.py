import random
from unittest import TestCase

from hamcrest import *

from chapter08.problem8_4 import jugs_group, jugs_match
from datastructures.array import Array


class TestProblem8_4(TestCase):

    def test_jugs_group(self):
        n = random.randint(1, 20)
        red_elements = [random.randrange(1000) for _ in range(n)]
        blue_elements = random.sample(red_elements, n)
        reds_array = Array(red_elements)
        blues_array = Array(blue_elements)

        jugs_group(reds_array, blues_array)

        assert_that(reds_array.elements, contains_inanyorder(*red_elements))
        assert_that(reds_array, is_(equal_to(blues_array)))

    def test_jugs_match(self):
        n = random.randint(1, 20)
        red_elements = [random.randrange(1000) for _ in range(n)]
        blue_elements = random.sample(red_elements, n)
        reds_array = Array(red_elements)
        blues_array = Array(blue_elements)

        jugs_match(reds_array, blues_array, 1, n)

        assert_that(reds_array.elements, contains_inanyorder(*red_elements))
        assert_that(reds_array, is_(equal_to(blues_array)))

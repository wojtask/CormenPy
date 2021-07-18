import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter08.problem8_4 import jugs_group, jugs_match
from datastructures.array import Array


class TestProblem8_4(TestCase):

    def test_jugs_group(self):
        n = random.randint(1, 20)
        reds_array = get_random_array(size=n)
        blues_array = Array(random.sample(reds_array.elements, n))
        reds_original = copy.deepcopy(reds_array)

        jugs_group(reds_array, blues_array)

        assert_that(reds_array, is_(equal_to(blues_array)))
        assert_that(reds_array, contains_inanyorder(*reds_original))

    def test_jugs_match(self):
        n = random.randint(1, 20)
        reds_array = get_random_array(size=n)
        blues_array = Array(random.sample(reds_array.elements, n))
        reds_original = copy.deepcopy(reds_array)

        jugs_match(reds_array, blues_array, 1, n)

        assert_that(reds_array, is_(equal_to(blues_array)))
        assert_that(reds_array, contains_inanyorder(*reds_original))

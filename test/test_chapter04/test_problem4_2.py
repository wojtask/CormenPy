import copy
import random
from unittest import TestCase

from hamcrest import *

from chapter04.problem4_2 import missing_integer
from datastructures.array import Array
from util import between


class TestProblem4_2(TestCase):

    def test_missing_integer(self):
        n = random.randint(1, 20)
        array = Array(random.sample(between(0, n), n))
        original = copy.deepcopy(array)

        actual_missing = missing_integer(array)

        expected_missing = [x for x in between(0, n) if x not in original][0]
        assert_that(actual_missing, is_(equal_to(expected_missing)))

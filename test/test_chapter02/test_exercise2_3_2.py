import random
from unittest import TestCase

from hamcrest import *

from chapter02.exercise2_3_2 import merge_
from datastructures.array import Array


class TestExercise2_3_2(TestCase):

    def test_merge_(self):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        elements1 = sorted([random.randrange(1000) for _ in range(n1)])
        elements2 = sorted([random.randrange(1000) for _ in range(n2)])
        array = Array(elements1 + elements2)

        merge_(array, 1, n1, n1 + n2)

        expected_array = Array(sorted(elements1 + elements2))
        assert_that(array, is_(equal_to(expected_array)))

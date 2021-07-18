import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter02.exercise2_3_2 import merge_


class TestExercise2_3_2(TestCase):

    def test_merge_(self):
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        array1 = get_random_array(size=n1)
        array2 = get_random_array(size=n2)
        array = array1.sort() + array2.sort()

        merge_(array, 1, n1, n1 + n2)

        expected_array = (array1 + array2).sort()
        assert_that(array, is_(equal_to(expected_array)))

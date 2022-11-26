import copy
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter17.problem17_1 import bit_reversal_permutation, rev, bit_reversal_permutation_
from util import between


class TestProblem17_1(TestCase):

    def test_bit_reversal_permutation(self):
        k = random.randint(0, 4)
        n = 2 ** k
        array = get_random_array(size=n, start=0)
        original = copy.deepcopy(array)

        bit_reversal_permutation(array)

        for i in between(0, n - 1):
            assert_that(array[i], is_(equal_to(original[rev(k, i)])))

    def test_bit_reversal_permutation_(self):
        k = random.randint(0, 4)
        n = 2 ** k
        array = get_random_array(size=n, start=0)
        original = copy.deepcopy(array)

        bit_reversal_permutation_(array)

        for i in between(0, n - 1):
            assert_that(array[i], is_(equal_to(original[rev(k, i)])))

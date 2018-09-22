import random
from unittest import TestCase

from hamcrest import *

from chapter17.problem17_1 import bit_reversal, rev, bit_reversal_
from datastructures.array import Array
from util import between


class TestProblem17_1(TestCase):

    def test_bit_reversal(self):
        k = random.randint(0, 4)
        n = 2 ** k
        elements = [random.randint(0, 999) for _ in range(n)]
        array = Array(elements, start=0)
        original_array = Array(elements, start=0)

        bit_reversal(array)

        for i in between(0, n - 1):
            assert_that(array[i], is_(equal_to(original_array[rev(k, i)])))

    def test_bit_reversal_(self):
        k = random.randint(0, 4)
        n = 2 ** k
        elements = [random.randint(0, 999) for _ in range(n)]
        array = Array(elements, start=0)
        original_array = Array(elements, start=0)

        bit_reversal_(array)

        for i in between(0, n - 1):
            assert_that(array[i], is_(equal_to(original_array[rev(k, i)])))

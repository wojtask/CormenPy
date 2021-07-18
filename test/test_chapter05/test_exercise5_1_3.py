from unittest import TestCase

from hamcrest import *

from chapter05.exercise5_1_3 import unbiased_random
from util import between


class TestExercise5_1_3(TestCase):

    def test_unbiased_random(self):
        samples = 1000
        count0 = 0
        for _ in between(1, samples):
            x = unbiased_random()
            assert_that(x, is_in([0, 1]))
            if x == 0:
                count0 += 1

        assert_that(count0 / samples, is_(close_to(0.5, 0.1)))

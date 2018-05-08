from unittest import TestCase

from hamcrest import *

from chapter05.exercise5_1_3 import unbiased_random


class TestExercise5_1_3(TestCase):

    def test_unbiased_random(self):
        samples = 1000
        count = [0, 0]
        for _ in range(samples):
            x = unbiased_random()
            assert_that(x, is_in([0, 1]))
            count[x] += 1

        assert_that(count[0], is_(close_to(count[1], samples // 10)))

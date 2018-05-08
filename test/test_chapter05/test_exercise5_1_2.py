from unittest import TestCase

from hamcrest import *

from chapter05.exercise5_1_2 import random


class TestExercise5_1_2(TestCase):

    def test_random(self):
        lower_bound = 10
        upper_bound = 20

        x = random(lower_bound, upper_bound)

        assert_that(x, is_(greater_than_or_equal_to(lower_bound)))
        assert_that(x, is_(less_than_or_equal_to(upper_bound)))

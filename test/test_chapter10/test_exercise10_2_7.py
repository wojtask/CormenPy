from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_7 import singly_linked_list_reverse
from list_util import get_random_singly_linked_list, get_linked_list_keys


class TestExercise10_2_7(TestCase):

    def test_singly_linked_list_reverse(self):
        list_, nodes, keys = get_random_singly_linked_list()

        singly_linked_list_reverse(list_)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = list(reversed(keys))
        assert_that(actual_keys, is_(equal_to(expected_keys)))

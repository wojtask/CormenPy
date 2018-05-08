import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_2 import singly_linked_list_push, singly_linked_list_pop
from list_util import get_random_singly_linked_list, get_linked_list_keys


class TestExercise10_2_2(TestCase):

    def test_singly_linked_list_push(self):
        list_, nodes, keys = get_random_singly_linked_list()
        x = random.randint(0, 999)

        singly_linked_list_push(list_, x)

        actual_keys = get_linked_list_keys(list_)
        expected_keys = [x] + keys
        assert_that(actual_keys, is_(equal_to(expected_keys)))

    def test_singly_linked_list_pop(self):
        list_, nodes, keys = get_random_singly_linked_list(max_size=5)

        actual_deleted = singly_linked_list_pop(list_)

        assert_that(actual_deleted, is_(equal_to(keys[0])))
        actual_keys = get_linked_list_keys(list_)
        expected_keys = keys[1:]
        assert_that(actual_keys, is_(equal_to(expected_keys)))

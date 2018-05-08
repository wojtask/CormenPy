import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_4 import list_search__
from list_util import get_random_doubly_linked_list_with_sentinel


class TestExercise10_2_4(TestCase):

    def test_list_search__(self):
        list_, nodes, keys = get_random_doubly_linked_list_with_sentinel(min_size=10, max_size=20, max_value=20)
        k = random.randint(1, 20)

        actual_node = list_search__(list_, k)

        if k in keys:
            assert_that(actual_node, is_in(nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(list_.nil))

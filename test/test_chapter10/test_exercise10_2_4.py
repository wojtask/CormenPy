import random
from unittest import TestCase

from hamcrest import *

from chapter10.exercise10_2_4 import list_search__
from list_util import get_random_doubly_linked_list_with_sentinel, \
    assert_doubly_linked_list_with_sentinel_structure_consistent


class TestExercise10_2_4(TestCase):

    def test_list_search__(self):
        linked_list = get_random_doubly_linked_list_with_sentinel(min_size=10, max_size=20, max_value=20)
        original_nodes = linked_list.as_nodes_array()
        original_keys = linked_list.as_keys_array()
        k = random.randint(1, 20)

        actual_node = list_search__(linked_list, k)

        if k in original_keys:
            assert_that(actual_node, is_in(original_nodes))
            assert_that(actual_node.key, is_(equal_to(k)))
        else:
            assert_that(actual_node, is_(linked_list.nil))
        actual_keys = linked_list.as_keys_array()
        assert_that(actual_keys, is_(equal_to(original_keys)))
        assert_doubly_linked_list_with_sentinel_structure_consistent(linked_list)

from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.textbook_problem6_1 import build_max_heap_
from heap_util import assert_max_heap


class TestTextbookProblem6_1(TestCase):

    def test_build_max_heap_(self):
        array, elements = get_random_array()

        build_max_heap_(array)

        assert_that(array, has_property('heap_size'))
        assert_that(array.heap_size, is_(equal_to(array.length)))
        assert_max_heap(array)

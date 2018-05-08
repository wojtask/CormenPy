import io
from contextlib import redirect_stdout
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter12.textbook_exercise12_3_3 import inorder_sort


class TestTextbookExercise12_3_3(TestCase):

    def test_inorder_sort(self):
        array, elements = get_random_array()
        captured_output = io.StringIO()

        with redirect_stdout(captured_output):
            inorder_sort(array)

        actual_output = [int(x) for x in captured_output.getvalue().splitlines()]
        assert_that(actual_output, is_(equal_to(sorted(elements))))

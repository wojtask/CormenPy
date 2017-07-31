import math
import random
from unittest import TestCase

from hamcrest import *

from array_util import get_random_array
from chapter06.ex6_2_2 import min_heapify
from chapter06.ex6_2_5 import iterative_max_heapify
from chapter06.ex6_5_3 import heap_minimum, heap_extract_min, heap_decrease_key, min_heap_insert
from chapter06.ex6_5_7 import max_heap_delete
from chapter06.pr6_2 import multiary_parent, multiary_child, multiary_max_heapify, multiary_heap_extract_max, \
    multiary_max_heap_insert, multiary_heap_increase_key
from chapter06.pr6_3 import young_extract_min, youngify, young_insert, young_sort, young_search
from datastructures.array import Array
from datastructures.matrix import Matrix
from heap_util import get_random_min_heap, assert_min_heap, get_random_max_heap, assert_max_heap


def random_young_tableau(max_rows=5, max_columns=5, max_value=999):
    threshold = 0.95 * max_value  # all numbers greater than threshold will be transformed to math.inf
    rows = random.randint(1, max_rows)
    columns = random.randint(1, max_columns)
    row = [random.randint(0, max_value) for _ in range(columns)]  # the first row
    data = [sorted([x if x <= threshold else math.inf for x in row])]
    for i in range(1, rows):
        if data[i - 1][0] < math.inf:
            row = [random.randint(data[i - 1][0], max_value)]
        else:
            row = [math.inf]
        for j in range(1, columns):
            bound = max(row[j - 1], data[i - 1][j])
            if bound < math.inf:
                row.append(random.randint(bound, max_value))
            else:
                row.append(math.inf)
        data.append(sorted([x if x <= threshold else math.inf for x in row]))
    return Matrix(data), data


def assert_young_tableau(matrix):
    m, n = matrix.rows, matrix.columns
    for j in range(2, n + 1):
        assert_that(matrix[1, j], is_(greater_than_or_equal_to(matrix[1, j - 1])))
    for i in range(2, m + 1):
        assert_that(matrix[i, 1], is_(greater_than_or_equal_to(matrix[i - 1, 1])))
        for j in range(2, n + 1):
            assert_that(matrix[i, j], is_(greater_than_or_equal_to(matrix[i, j - 1])))
            assert_that(matrix[i, j], is_(greater_than_or_equal_to(matrix[i - 1, j])))


class Solutions06Test(TestCase):

    def test_min_heapify(self):
        heap, data = get_random_min_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] = data[i - 1] = random.randint(heap[i], 999)  # randomly increase value of randomly chosen element

        min_heapify(heap, i)

        assert_that(heap.heap_size, is_(equal_to(len(data))))
        assert_min_heap(heap)
        assert_that(heap.data, contains_inanyorder(*data))

    def test_iterative_max_heapify(self):
        heap, data = get_random_max_heap()
        i = random.randint(1, heap.heap_size)
        heap[i] = data[i - 1] = random.randint(0, heap[i])  # randomly decrease value of randomly chosen element

        iterative_max_heapify(heap, i)

        assert_that(heap.heap_size, is_(equal_to(len(data))))
        assert_max_heap(heap)
        assert_that(heap.data, contains_inanyorder(*data))

    def test_heap_minimum(self):
        heap, data = get_random_min_heap()

        actual_min = heap_minimum(heap)

        assert_that(actual_min, is_(equal_to(min(data))))

    def test_extract_min(self):
        heap, data = get_random_min_heap()

        actual_min = heap_extract_min(heap)

        assert_that(actual_min, is_(equal_to(min(data))))
        assert_min_heap(heap)
        actual_heap_keys = heap[1:heap.heap_size]
        expected_heap_keys = sorted(data)[1:]  # all but minimum
        assert_that(actual_heap_keys, contains_inanyorder(*expected_heap_keys))

    def test_heap_decrease_key(self):
        heap, data = get_random_min_heap()
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)

        if new_key > old_key:
            assert_that(calling(heap_decrease_key).with_args(heap, i, new_key),
                        raises(RuntimeError, 'new key is larger than current key'))
        else:
            heap_decrease_key(heap, i, new_key)

            assert_that(heap.heap_size, is_(equal_to(len(data))))
            expected_heap_keys = list(data)
            expected_heap_keys.remove(old_key)
            expected_heap_keys.append(new_key)
            assert_that(heap.data, contains_inanyorder(*expected_heap_keys))

    def test_min_heap_insert(self):
        heap, data = get_random_min_heap()
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        min_heap_insert(heap, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(data) + 1)))
        assert_min_heap(heap)
        expected_heap_keys = data + [new_key]
        assert_that(heap.data, contains_inanyorder(*expected_heap_keys))

    def test_max_heap_delete(self):
        heap, data = get_random_max_heap()
        i = random.randint(1, heap.heap_size)
        key_to_delete = heap[i]

        actual_deleted_key = max_heap_delete(heap, i)

        assert_that(actual_deleted_key, is_(equal_to(key_to_delete)))
        assert_max_heap(heap)
        actual_heap_keys = heap[1:heap.heap_size]
        expected_heap_keys = list(data)
        expected_heap_keys.remove(key_to_delete)
        assert_that(actual_heap_keys, contains_inanyorder(*expected_heap_keys))

    def test_multiary_parent_child(self):
        d = random.randint(2, 7)
        i = random.randint(1, 30)

        for k in range(1, d + 1):
            assert_that(multiary_parent(d, multiary_child(d, i, k)), is_(equal_to(i)))

    def test_multiary_max_heapify(self):
        ary = random.randint(2, 7)
        heap, data = get_random_max_heap(ary=ary)
        i = random.randint(1, heap.heap_size)
        heap[i] = data[i - 1] = random.randint(0, heap[i])  # randomly decrease value of randomly chosen element

        multiary_max_heapify(heap, ary, i)

        assert_that(heap.heap_size, is_(equal_to(len(data))))
        assert_max_heap(heap, ary=ary)
        assert_that(heap.data, contains_inanyorder(*data))

    def test_multiary_heap_extract_max(self):
        ary = random.randint(2, 7)
        heap, data = get_random_max_heap(ary=ary)

        actual_max = multiary_heap_extract_max(heap, ary)

        assert_that(actual_max, is_(equal_to(max(data))))
        assert_max_heap(heap, ary=ary)
        actual_heap_keys = heap[1:heap.heap_size]
        expected_heap_keys = sorted(data)[:-1]  # all but maximum
        assert_that(actual_heap_keys, contains_inanyorder(*expected_heap_keys))

    def test_multiary_max_heap_insert(self):
        ary = random.randint(2, 7)
        heap, data = get_random_max_heap(ary=ary)
        heap.data.append(None)  # to increase the heap's capacity for the new element
        heap.length += 1
        new_key = random.randrange(1000)

        multiary_max_heap_insert(heap, ary, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(data) + 1)))
        assert_max_heap(heap, ary=ary)
        expected_heap_keys = data + [new_key]
        assert_that(heap.data, contains_inanyorder(*expected_heap_keys))

    def test_multiary_heap_increase_key(self):
        ary = random.randint(2, 7)
        heap, data = get_random_max_heap(ary=ary)
        i = random.randint(1, heap.heap_size)
        old_key = heap[i]
        new_key = random.randrange(1000)
        real_new_key = max(old_key, new_key)

        multiary_heap_increase_key(heap, ary, i, new_key)

        assert_that(heap.heap_size, is_(equal_to(len(data))))
        assert_max_heap(heap, ary=ary)
        expected_heap_keys = list(data)
        expected_heap_keys.remove(old_key)
        expected_heap_keys.append(real_new_key)
        assert_that(heap.data, contains_inanyorder(*expected_heap_keys))

    def test_young_extract_min(self):
        young, data = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not empty
        if young[1, 1] == math.inf:
            young[1, 1] = data[0][0] = random.randrange(1000)

        actual_min = young_extract_min(young, m, n, 1, 1)

        assert_young_tableau(young)
        assert_that(actual_min, is_(equal_to(min(min(row for row in data)))))
        actual_data = [x for row in young.data for x in row]
        expected_data = [x for row in data for x in row]
        expected_data.remove(actual_min)
        expected_data.append(math.inf)
        assert_that(actual_data, contains_inanyorder(*expected_data))

    def test_youngify(self):
        young, data = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = data[m - 1][n - 1] = math.inf

        # randomly decrease value of randomly chosen element
        i = random.randint(1, m)
        j = random.randint(1, n)
        if young[i, j] < math.inf:
            young[i, j] = data[i - 1][j - 1] = random.randint(0, young[i, j])

        youngify(young, i, j)

        assert_young_tableau(young)
        actual_data = [x for row in young.data for x in row]
        expected_data = [x for row in data for x in row]
        assert_that(actual_data, contains_inanyorder(*expected_data))

    def test_young_insert(self):
        young, data = random_young_tableau()
        m, n = young.rows, young.columns
        # make sure the young tableau is not full
        if young[m, n] < math.inf:
            young[m, n] = data[m - 1][n - 1] = math.inf

        new_key = random.randint(0, 999)

        young_insert(young, m, n, new_key)

        assert_young_tableau(young)
        actual_data = [x for row in young.data for x in row]
        expected_data = [x for row in data for x in row]
        expected_data.remove(math.inf)
        expected_data.append(new_key)
        assert_that(actual_data, contains_inanyorder(*expected_data))

    def test_young_sort(self):
        n = random.randint(1, 5)
        array, data = get_random_array(min_size=n * n, max_size=n * n)

        young_sort(array)

        expected_array = Array(sorted(data))
        assert_that(array, is_(equal_to(expected_array)))

    def test_young_search(self):
        young, data = random_young_tableau(max_value=20)
        m, n = young.rows, young.columns
        v = random.randint(0, 20)

        actual_found = young_search(young, m, n, v)

        if v in [x for row in data for x in row]:
            assert_that(actual_found, is_(True))
        else:
            assert_that(actual_found, is_(False))

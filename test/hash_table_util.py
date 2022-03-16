import random

from hamcrest import *

from array_util import get_random_array
from chapter11.exercise11_4_2 import Deleted
from datastructures.array import Array
from datastructures.hash_table import Element, ChainedElement
from util import between


def get_random_direct_address_table():
    table_size = random.randint(1, 10)
    nelements = random.randint(0, table_size)
    keys = get_random_array(size=nelements, max_value=table_size - 1, unique=True)
    elements = Array(Element(key) for key in keys)
    table = Array.indexed(0, table_size - 1)
    for element in elements:
        table[element.key] = element
    return table


def get_random_bit_vector():
    bit_vector_size = random.randint(1, 10)
    nelements = random.randint(0, bit_vector_size)
    keys = get_random_array(size=nelements, max_value=bit_vector_size, unique=True)
    bit_vector = Array((1 if i in keys else 0 for i in between(1, bit_vector_size)), start=0)
    return bit_vector


def get_random_chained_direct_address_table():
    table_size = random.randint(1, 10)
    nelements = random.randint(0, table_size)
    keys = get_random_array(size=nelements, max_value=table_size - 1)
    elements = Array(ChainedElement(key) for key in keys)
    table = Array.indexed(0, table_size - 1)

    for element in elements:
        list_ = table[element.key]
        if list_:
            list_.prev = element
        element.next = list_
        table[element.key] = element
    return table


def get_random_chained_hash_table(max_value=999):
    table_size = random.randint(1, 10)
    nelements = random.randint(0, 3 * table_size)
    keys = get_random_array(size=nelements, max_value=max_value)
    elements = Array(ChainedElement(key) for key in keys)
    table = Array.indexed(0, table_size - 1)
    h = modular_hash

    for element in elements:
        list_ = table[h(element.key, table_size)]
        if list_:
            list_.prev = element
        element.next = list_
        table[h(element.key, table_size)] = element
    return table, h


def get_chained_hash_table_elements(table):
    elements = Array()
    for list_ in table:
        x = list_
        while x is not None:
            elements.append(x)
            x = x.next
    return elements


def get_random_huge_array(max_value=999):
    capacity = random.randint(1, min(20, max_value))
    nelements = random.randint(0, capacity)
    huge_array = Array.indexed(0, max_value)
    stack_array = Array.indexed(1, capacity)
    keys = get_random_array(size=nelements, max_value=max_value, unique=True)

    for i, key in enumerate(keys, start=1):
        huge_array[key] = i
        stack_array[i] = Element(key)
    stack_array.top = keys.length

    return huge_array, stack_array, keys


def assert_huge_array_consistent(huge_array, stack_array):
    for i, element in enumerate(stack_array[1:stack_array.top], start=1):
        assert_that(huge_array[element.key], is_(equal_to(i)))


def get_random_hash_table_linear_probing(max_value=999):
    table_size = random.randint(1, 10)
    table, keys = random_hash_table(linear_hash, table_size, max_value)
    return table, keys, linear_hash


def get_random_hash_table_quadratic_probing(max_value=999):
    # make sure the table size is a power of 2
    table_size = random.choice([2 ** n for n in between(0, 5)])
    table, keys = random_hash_table(quadratic_hash, table_size, max_value)
    return table, keys, modular_hash


def modular_hash(k, m):
    return k % m


def linear_hash(k, i, m):
    return (modular_hash(k, m) + i) % m


def quadratic_hash(k, i, m):
    return (modular_hash(k, m) + i * (i + 1) // 2) % m


def random_hash_table(h, table_size, max_value):
    table = Array.indexed(0, table_size - 1)
    nelements = random.randint(0, table.length)
    keys = get_random_array(size=nelements, max_value=max_value)
    for key in keys:
        i = 0
        while table[h(key, i, table_size)] is not None:
            i += 1
        table[h(key, i, table_size)] = key
    return table, keys


def get_hash_table_keys(table):
    return Array(key for key in table if key is not None and key is not Deleted)

import random

from hamcrest import *

from array_util import get_random_array
from chapter11.exercise11_4_2 import Deleted
from datastructures.array import Array
from datastructures.essential import Element
from datastructures.hash_table import ChainedElement
from util import between


def modular_hash(m):
    return lambda k: k % m


def linear_hash(m):
    return lambda k, i: (modular_hash(m)(k) + i) % m


def quadratic_hash(m):
    return lambda k, i: (modular_hash(m)(k) + i * (i + 1) // 2) % m


def get_random_direct_address_table():
    table_size = random.randint(1, 10)
    nelements = random.randint(0, table_size)
    keys = get_random_array(size=nelements, max_value=table_size - 1, unique=True)
    elements = Array(Element(key) for key in keys)
    table = Array.indexed(0, table_size - 1)
    for element in elements:
        table[element.key] = element
    return table.save_state()


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
        head = table[element.key]
        if head is not None:
            head.prev = element
        element.next = head
        table[element.key] = element
    return table.save_state()


def get_random_chained_hash_table(max_value=999):
    table_size = random.randint(1, 10)
    nelements = random.randint(0, 3 * table_size)
    keys = get_random_array(size=nelements, max_value=max_value)
    elements = Array(ChainedElement(key) for key in keys)
    table = Array.indexed(0, table_size - 1)
    h = modular_hash(table_size)

    for element in elements:
        head = table[h(element.key)]
        if head is not None:
            head.prev = element
        element.next = head
        table[h(element.key)] = element
    return table.save_state(), h


def get_chained_hash_table_elements(table):
    elements = Array()
    for head in table:
        x = head
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

    return huge_array.save_state(), stack_array.save_state()


def assert_huge_array_consistent(huge_array, stack_array):
    for i, element in enumerate(stack_array[:stack_array.top], start=1):
        assert_that(huge_array[element.key], is_(equal_to(i)))


def get_random_hash_table_linear_probing(max_value=999):
    table_size = random.randint(1, 10)
    hash_function = linear_hash(table_size)
    table = random_hash_table(hash_function, table_size, max_value)
    return table, hash_function


def get_random_hash_table_quadratic_probing(max_value=999):
    # make sure the table size is a power of 2
    table_size = random.choice([2 ** n for n in between(0, 5)])
    table = random_hash_table(quadratic_hash(table_size), table_size, max_value)
    return table, modular_hash(table_size)


def random_hash_table(h, table_size, max_value):
    table = Array.indexed(0, table_size - 1)
    nelements = random.randint(0, table.length)
    keys = get_random_array(size=nelements, max_value=max_value)
    for key in keys:
        i = 0
        while table[h(key, i)] is not None:
            i += 1
        table[h(key, i)] = key
    return table.save_state()


def get_hash_table_keys(table):
    return Array(key for key in table if key is not None and key is not Deleted)

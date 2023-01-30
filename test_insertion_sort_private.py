#
# Write here the tests for Insertion Sort
#

from insertion_sort import sort

import random
import pytest

@pytest.mark.timeout(5)
def test_sort_empty_list():
    the_list_to_sort = []
    sorted_list = sort(the_list_to_sort)
    assert sorted_list == []


@pytest.mark.timeout(5)
def test_sort_one_list_positive():
    the_list_to_sort = [1]
    sorted_list = sort(the_list_to_sort)
    assert sorted_list == [1]


@pytest.mark.timeout(5)
def test_sort_one_list_negative():
    the_list_to_sort = [-1]
    sorted_list = sort(the_list_to_sort)
    assert sorted_list == [-1]


@pytest.mark.timeout(5)
def test_sort_small():
    the_list_to_sort = [1, -1, 0]
    sorted_list = sort(the_list_to_sort)
    assert sorted_list == [-1, 0, 1]


@pytest.mark.timeout(120)
def test_many_random_lists():
    for i in [50, 100, 200]:
        # Make bigger and bigger lists
        the_list_to_sort = random.sample(range(-1000, 1000), i * 2)
        sorted_list = sort(the_list_to_sort)
        # The sorted() function returns a sorted list of the specified iterable object.
        sorted_with_python = sorted(the_list_to_sort)
        assert sorted_list == sorted_with_python
#
# Write here the tests for Insertion Sort
#

from insertion_sort import sort



def test_sort_a_list():
    """
    Test the implementation with a short list containing no duplicates
    """
    the_list_to_sort = [1, 5, 2, 10, 3]
    sorted_list = sort(the_list_to_sort)
    assert sorted_list == [1, 2, 3, 5, 10]


def test_sort_a_sorted_list():
    """
    Test the implementation with an already sorted list
    """
    already_sorted = [1, 2, 3]
    sorted_list = sort(already_sorted)
    assert sorted_list == already_sorted

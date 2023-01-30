#
# Write here the tests for the Double Linked List
#
import pytest

from double_linked_list import DoubleLinkedList


def test_insert_at_beginning_with_empty_list():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(5)
    assert dll.size() == 1
    assert dll.get_first() == 5
    assert dll.get_last() == 5


def test_insert_at_right_position():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(10)
    dll.insert_at_position(3, position=0)
    assert dll.size() == 2
    assert dll.get_first() == 3
    assert dll.get_last() == 10


def test_insert_at_right_position_in_empty_list():
    dll = DoubleLinkedList()
    dll.insert_at_position(3, position=0)
    assert dll.size() == 1
    assert dll.get_first() == 3
    assert dll.get_last() == 3

def test_insert_at_position_1():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    dll.insert_at_position(2, position=1)
    assert dll.print_forward() == "1,2,3,4,5"


def test_insert_at_wrong_position():
    with pytest.raises(ValueError):
        dll = DoubleLinkedList()
        dll.insert_at_beginning(5)
        dll.insert_at_position(5, position=10)


def test_insert_at_end_with_empty_list():
    dll = DoubleLinkedList()
    dll.insert_at_end(2)
    assert dll.size() == 1
    assert dll.get_first() == 2
    assert dll.get_last() == 2


def test_insert_in_front_and_delete_from_front():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(4)
    dll.delete_at_beginning()
    assert dll.size() == 0


def test_insert_in_front_and_delete_from_back():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(7)
    dll.delete_at_end()
    assert dll.size() == 0


def test_many_insert_and_many_delete():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(4)
    dll.insert_at_end(4)
    dll.delete_at_beginning()
    dll.delete_at_end()
    assert dll.size() == 0

def test_delete_at_position():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.delete_at_position(1)
    assert dll.size() == 1
    assert dll.get_first() == 2
    assert dll.get_last() == 2

def test_delete_at_0_position():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.delete_at_position(0)
    assert dll.size() == 0

def test_delete_at_wrong_position():
    with pytest.raises(ValueError):
        dll = DoubleLinkedList()
        dll.insert_at_beginning(5)
        dll.insert_at_position(5, position=10)

def test_print_forward():
    """
    Test that the Double Linked List prints values comma-separated without spaces in the same order
    """
    dll = DoubleLinkedList()

    dll.insert_at_end(1)
    # [1]
    dll.insert_at_end(2)
    # [1, 2]
    dll.insert_at_end(3)
    # [1, 2, 3]
    assert dll.print_forward() == "1,2,3"

def test_print_empty_list_forward():
    dll = DoubleLinkedList()
    assert dll.print_forward() == None

def test_print_backward():
    """
    Test that the Double Linked List prints values comma-separated without spaces in reverse order
    """
    dll = DoubleLinkedList()

    dll.insert_at_beginning(1)
    # [1]
    dll.insert_at_beginning(2)
    # [2, 1]
    dll.insert_at_beginning(3)
    # [3, 2, 1]

    assert dll.print_backward() == "1,2,3"

def test_print_empty_list_backwards():
    dll = DoubleLinkedList()
    assert dll.print_backward() == None

def test_get_first_and_last_with_empty_list():
    dll = DoubleLinkedList()
    assert dll.get_first() == None
    assert dll.get_last() == None

def test_get_next_node():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    assert dll.get_next_node(2) == 3

def test_get_previous_node():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    assert dll.get_previous_node(2) == 1

def test_get_wrong_next_node():
    with pytest.raises(ValueError):
        dll = DoubleLinkedList()
        dll.insert_at_beginning(5)
        dll.get_next_node(7)

def test_get_wrong_previous_node():
    with pytest.raises(ValueError):
        dll = DoubleLinkedList()
        dll.insert_at_beginning(5)
        dll.get_previous_node(7)

def test_contains():
    dll = DoubleLinkedList()
    dll.insert_at_end(1)
    dll.insert_at_end(2)
    dll.insert_at_end(3)
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    assert dll.contains(2) == True
    assert dll.contains(7) == False

def test_contains_in_empty_list():
    dll=DoubleLinkedList()
    assert dll.contains(10) == False
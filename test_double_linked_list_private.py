#
# Write here the tests for the Double Linked List
#
import pytest

from double_linked_list import DoubleLinkedList

# Note: The operations must raise a ValueError when provided with inappropriate parameters.
# For instance, deleting an element from an empty list, removing/inserting at position outside the range [0, size() ) (0 included, size() excluded).
@pytest.mark.timeout(5)
def test_insert_at_invalid_positions_with_empty_list():
    dll = DoubleLinkedList()

    with pytest.raises(ValueError):
        dll.insert_at_position(4, -1)

    with pytest.raises(ValueError):
        dll.insert_at_position(4, 0)

    with pytest.raises(ValueError):
        dll.insert_at_position(4, 1)


@pytest.mark.timeout(5)
def test_insert_at_invalid_positions_with_singleton_list():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1) # Size 1, Pos 0

    with pytest.raises(ValueError):
        dll.insert_at_position(4, -1)


@pytest.mark.timeout(5)
def test_insert_at_invalid_positions_with_nonempty_list():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)  # Size 1, Pos 0
    dll.insert_at_beginning(10)  # Size 2, Pos 1

    # Cannot insert at position == size()
    with pytest.raises(ValueError):
        dll.insert_at_position(4, position=2)

    # Do not raise exception
    dll.insert_at_position(4, 1)


@pytest.mark.timeout(5)
def test_insert_at_beginning_starting_from_empty_list():
    dll = DoubleLinkedList()
    assert dll.size() == 0

    dll.insert_at_beginning(5)
    assert dll.size() == 1

    assert dll.get_first() == 5
    assert dll.get_last() == 5

    dll.insert_at_beginning(10)
    assert dll.size() == 2

    assert dll.get_first() == 10
    assert dll.get_last() == 5

    dll.insert_at_beginning(15)
    assert dll.size() == 3

    assert dll.get_first() == 15
    assert dll.get_last() == 5


@pytest.mark.timeout(5)
def test_insert_at_end_starting_from_empty_list():
    dll = DoubleLinkedList()
    assert dll.size() == 0

    dll.insert_at_end(5)
    assert dll.size() == 1

    assert dll.get_first() == 5
    assert dll.get_last() == 5

    dll.insert_at_end(10)
    assert dll.size() == 2

    assert dll.get_first() == 5
    assert dll.get_last() == 10

    dll.insert_at_end(15)
    assert dll.size() == 3

    assert dll.get_first() == 5
    assert dll.get_last() == 15


@pytest.mark.timeout(5)
def test_insert_at_position():
    dll = DoubleLinkedList()

    dll.insert_at_beginning(10)  # Size 1
    head = dll.get_first_node()
    tail = dll.get_last_node()
    assert head == tail

    dll.insert_at_end(5)  # Size 2
    new_head = dll.get_first_node()
    new_tail = dll.get_last_node()

    assert new_head == head
    assert new_tail != tail
    assert new_tail != head

    dll.insert_at_position(3, position=1)  # Size 3
    new_head = dll.get_first_node()
    old_tail = new_tail
    new_tail = dll.get_last_node()

    assert new_head == head
    assert new_tail == old_tail

    assert dll.size() == 3
    assert dll.get_first() == 10
    assert dll.get_last() == 5

    assert dll.print_forward() == "10,3,5"
    assert dll.print_backward() == "5,3,10"

    # Assert the second node
    assert dll.get_next_node(dll.get_first_node()) == dll.get_previous_node(dll.get_last_node())
    # Assert the last node
    assert dll.get_next_node(dll.get_next_node(dll.get_first_node())) == dll.get_last_node()

@pytest.mark.timeout(5)
def test_insert_even_more_at_position():
    dll = DoubleLinkedList()

    dll.insert_at_beginning(10)  # Size 1
    dll.insert_at_end(5)  # Size 2
    dll.insert_at_position(3, position=1)  # Size 3

    dll.insert_at_position(33, position=1)
    # 10 -- 33 -- 3 -- 5
    assert dll.size() == 4
    assert dll.get_first() == 10
    assert dll.get_last() == 5

    # Assert the second node, 33
    assert dll.get_next_node(dll.get_first_node()) == dll.get_previous_node(dll.get_previous_node(dll.get_last_node()))

    dll.insert_at_position(333, position=1)

    assert dll.size() == 5
    assert dll.get_first() == 10
    assert dll.get_last() == 5

    assert dll.print_forward() == "10,333,33,3,5"
    assert dll.print_backward() == "5,3,33,333,10"


@pytest.mark.timeout(5)
def test_delete_at_beginning_from_empty():
    dll = DoubleLinkedList()
    with pytest.raises(ValueError):
        dll.delete_at_beginning()


@pytest.mark.timeout(5)
def test_delete_at_end_from_empty():
    dll = DoubleLinkedList()
    with pytest.raises(ValueError):
        dll.delete_at_end()


@pytest.mark.timeout(5)
def test_delete_before_head_invalid_position():
    """
        Removing/inserting at position outside the range [0, size() ) (0 included, size() excluded)
        must raise a ValueError
    :return:
    """
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)  # Size 1
    dll.insert_at_beginning(10)  # Size 2

    with pytest.raises(ValueError):
        dll.delete_at_position(-1)


@pytest.mark.timeout(5)
def test_delete_at_invalid_position():
    """
        Removing/inserting at position outside the range [0, size() ) (0 included, size() excluded)
        must raise a ValueError
    :return:
    """
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)  # Size 1
    dll.insert_at_beginning(10)  # Size 2

    with pytest.raises(ValueError):
        dll.delete_at_position(2)


@pytest.mark.timeout(5)
def test_delete_at_valid_positions():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(1)  # Size 1
    dll.delete_at_position(0)

    assert dll.size() == 0

    dll.insert_at_beginning(30)  # Size 1
    dll.insert_at_beginning(20)  # Size 2
    dll.insert_at_beginning(10)  # Size 3

    dll.delete_at_position(1)

    assert dll.size() == 2
    assert dll.get_first() == 10
    assert dll.get_last() == 30

    assert dll.print_forward() == "10,30"

    dll.delete_at_position(1)
    assert dll.size() == 1

    assert dll.get_first() == 10
    assert dll.get_last() == 10

    assert dll.print_forward() == "10"


@pytest.mark.timeout(5)
def test_insert_at_wrong_position():
    with pytest.raises(ValueError):
        dll = DoubleLinkedList()
        dll.insert_at_beginning(5)
        dll.insert_at_position(5, position=10)


@pytest.mark.timeout(5)
def test_insert_at_end_with_empty_list():
    dll = DoubleLinkedList()
    dll.insert_at_end(2)
    assert dll.size() == 1
    assert dll.get_first() == 2
    assert dll.get_last() == 2


@pytest.mark.timeout(5)
def test_insert_in_front_and_delete_from_front():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(4)
    dll.delete_at_beginning()
    assert dll.size() == 0


@pytest.mark.timeout(5)
def test_insert_in_front_and_delete_from_back():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(7)
    dll.delete_at_end()
    assert dll.size() == 0


@pytest.mark.timeout(5)
def test_many_insert_and_many_delete():
    dll = DoubleLinkedList()
    dll.insert_at_beginning(4)
    dll.insert_at_end(4)
    dll.delete_at_beginning()
    dll.delete_at_end()
    assert dll.size() == 0


@pytest.mark.timeout(5)
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


@pytest.mark.timeout(5)
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


@pytest.mark.timeout(5)
def test_contains_missing():
    dll = DoubleLinkedList()
    assert dll.contains(3) == False

    dll.insert_at_end(5)
    assert dll.contains(3) == False

    dll.delete_at_end()
    assert dll.contains(3) == False


@pytest.mark.timeout(5)
def test_does_not_contains_if_removed():
    dll = DoubleLinkedList()

    dll.insert_at_end(3)
    assert dll.contains(3) == True

    dll.insert_at_end(5)
    assert dll.contains(3) == True

    dll.delete_at_beginning()
    assert dll.contains(3) == False


@pytest.mark.timeout(5)
def test_does_not_contains_head_if_removed():
    dll = DoubleLinkedList()

    dll.insert_at_end(3)
    assert dll.size() == 1
    head = dll.get_first_node()

    dll.delete_at_beginning()
    assert dll.size() == 0
    assert dll.get_first_node() != head


@pytest.mark.timeout(5)
def test_does_not_contains_node_if_removed():
    dll = DoubleLinkedList()

    dll.insert_at_end(3)  # Pos 0
    dll.insert_at_end(4)  # Pos 1
    dll.insert_at_end(5)  # Pos 2
    dll.insert_at_end(6)  # Pos 3

    assert dll.contains(4) == True

    dll.delete_at_end()
    assert dll.contains(4) == True

    dll.delete_at_position(position=1)
    assert dll.contains(4) == False

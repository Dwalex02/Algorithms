#
# Write here the tests for the Move to Back Program
#
import string
import pytest

# Add tests for the Linked List
from move_to_back import MoveToBack, LinkedList


@pytest.mark.timeout(5)
def test_empty_list():
    ll = LinkedList()
    assert "" == ll.print()


@pytest.mark.timeout(5)
def test_insert_elements():
    ll = LinkedList()
    ll.insert(1)
    assert "1" == ll.print()
    ll.insert('a')
    assert "1,a" == ll.print()
    ll.insert('b')
    assert "1,a,b" == ll.print()


@pytest.mark.timeout(5)
def test_delete_missing():
    ll = LinkedList()
    ll.delete("3")
    assert "" == ll.print()


@pytest.mark.timeout(5)
def test_delete_heads():
    ll = LinkedList()
    # The following is ok since we are in unit test
    ll.insert(1)
    ll.insert('a')

    ll.delete(ll.head)
    assert "a"== ll.print()

    ll.delete(ll.head)
    assert "" == ll.print()


@pytest.mark.timeout(5)
def test_insert_and_delete():
    ll = LinkedList()
    ll.insert(1)
    assert "1" == ll.print()
    ll.insert('a')
    assert "1,a" == ll.print()
    ll.insert('b')
    assert "1,a,b" == ll.print()
    ll.delete(ll.head)
    assert "a,b" == ll.print()
    ll.insert('b')
    assert "a,b,b" == ll.print()

@pytest.mark.timeout(5)
def test_empty():
    mtb = MoveToBack()
    assert mtb.get_sequence() == ""


@pytest.mark.timeout(5)
def test_insert_without_repetitions():
    # Same as a stack
    expected_output = []
    mtb = MoveToBack()
    for c in ['a', 'b', 'c', 'd']:
        mtb.insert(c)
        expected_output.append(c)

    assert ",".join(expected_output) == mtb.get_sequence()


@pytest.mark.timeout(5)
def test_insert_complex():

    mtb = MoveToBack()
    for l in list(string.ascii_lowercase):
        mtb.insert(l)

    assert ",".join(list(string.ascii_lowercase)) == mtb.get_sequence()

    expected_list = string.ascii_lowercase
    for c in list("panama"):
         mtb.insert(c)
         expected_list = expected_list.replace(c, "") + c
         assert ",".join(list(expected_list)) == mtb.get_sequence()
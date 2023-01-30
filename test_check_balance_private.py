#
# Write here the tests for the Balance Checker
#
from check_balance import is_balanced
import pytest

@pytest.mark.timeout(5)
def test_empty():
    assert is_balanced("") == True


@pytest.mark.timeout(5)
def test_only_open():
    assert is_balanced("(") == False
    assert is_balanced("((") == False
    assert is_balanced("(((") == False
    assert is_balanced("[") == False
    assert is_balanced("[[") == False
    assert is_balanced("[[[") == False
    assert is_balanced("{") == False
    assert is_balanced("{{") == False
    assert is_balanced("{{{") == False


@pytest.mark.timeout(5)
def test_only_closed():
    assert is_balanced(")") == False
    assert is_balanced("))") == False
    assert is_balanced("]") == False
    assert is_balanced("]]") == False
    assert is_balanced("}") == False
    assert is_balanced("}}") == False


@pytest.mark.timeout(5)
def test_is_not_balanced_if_different():
    assert is_balanced("(}") == False
    assert is_balanced("(]") == False
    assert is_balanced("[)") == False
    assert is_balanced("[}") == False
    assert is_balanced("{)") == False
    assert is_balanced("{]") == False


@pytest.mark.timeout(5)
def test_is_almost_balanced():
    assert is_balanced("((())") == False
    assert is_balanced("(()))") == False


@pytest.mark.timeout(5)
def test_is_balanced_with_different_parentheses():
    assert is_balanced("{}[]()") == True
    assert is_balanced("({}[]())") == True
    assert is_balanced("{{}[]()}") == True
    assert is_balanced("[{}[]()]") == True


@pytest.mark.timeout(5)
def test_with_random_chars():
    assert is_balanced(" {    }  [  ] ( )    ") == True
    assert is_balanced("asda{d{dasd}a  [dsad///](dsdasq)\n\n\n}") == True
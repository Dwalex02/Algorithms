#
# Write here the tests for the Balance Checker
#
from check_balance import is_balanced


def test_is_balanced():
    assert is_balanced("()") == True


def test_is_balanced_with_different_parentheses():
    assert is_balanced("[()]{}{[]([])}") == True


def test_is_not_balanced():
    assert is_balanced("(") == False


def test_is_not_balanced_1():
    assert is_balanced("()(") == False


def test_is_not_balanced_2():
    assert is_balanced("(()") == False


def test_is_not_balanced_with_different_parentheses():
    assert is_balanced("{)") == False


def test_wrong_nesting():
    assert is_balanced("{[}]") == False

def empty_string():
    assert is_balanced("") == False
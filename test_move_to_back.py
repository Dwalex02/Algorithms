#
# Write here the tests for the Move to Back Program
#

from move_to_back import MoveToBack


def test_move_to_back_smoke_test():
    mtb = MoveToBack()
    assert mtb.get_sequence() == ""

    mtb.insert("a")
    assert mtb.get_sequence() == "a"

    mtb.insert("a")
    assert mtb.get_sequence() == "a"

    mtb.insert("b")
    assert mtb.get_sequence() == "a,b"

    mtb.insert("a")
    assert mtb.get_sequence() == "b,a"


"""Array tests"""


from array import Array
import pytest


def test_getitem_setitem():
    """Check retrieving and inserting information to array"""
    lst = Array(5)

    assert lst[0] is None
    with pytest.raises(IndexError):
        assert lst[100] is None

    lst[0] = "zero"
    lst[4] = "five"

    assert lst[0] == "zero"
    assert lst[4] == "five"


def test_iter():
    """Check iterating throught array"""
    lst = Array(5)
    for item in lst:
        assert item is None

    lst[0] = 0
    lst[1] = 1
    lst[2] = 2
    lst[3] = 3
    lst[4] = 4

    for num, item in enumerate(lst):
        assert num == item

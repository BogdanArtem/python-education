"""Linked list tests"""

import pytest
from linked_list import LinkedList


def test_linked_list_pop_append():
    """Add the 'The quick brown fox jumps over the lazy dog' to linked list"""
    lst = LinkedList()

    lst.append("first")
    lst.append("second")
    lst.append("third")
    lst.append("fourth")

    assert lst.pop() == "fourth"
    assert lst.pop() == "third"
    assert lst.pop() == "second"
    assert lst.pop() == "first"

def test_linked_list_prepend_popleft():
    """Add the 'The quick brown fox jumps over the lazy dog' to linked list"""
    lst = LinkedList()

    lst.prepend("first")
    lst.prepend("second")
    lst.prepend("third")
    lst.prepend("fourth")

    assert lst.popleft() == "fourth"
    assert lst.popleft() == "third"
    assert lst.popleft() == "second"
    assert lst.popleft() == "first"


def test_linked_list_remove_empty():
    """Test that list raises error if pop or popleft are called"""
    lst = LinkedList()
    with pytest.raises(TypeError):
        lst.popleft()

    with pytest.raises(TypeError):
        lst.pop()

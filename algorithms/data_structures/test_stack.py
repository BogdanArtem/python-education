"""Tests for queue implementation"""


import pytest
from stack import Stack


def test_queue():
    """Add the 'The quick brown fox jumps over the lazy dog' to linked list"""
    lst = Stack()

    lst.push("first")
    lst.push("second")
    lst.push("third")
    lst.push("fourth")

    assert lst.pop() == "fourth"
    assert lst.pop() == "third"
    assert lst.pop() == "second"
    assert lst.pop() == "first"


def test_empty_dequeue():
    """Test that list raises error if pop or popleft are called"""
    lst = Stack()
    with pytest.raises(TypeError):
        lst.pop()

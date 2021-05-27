"""Tests for queue implementation"""


from queue import Queue
import pytest


def test_queue():
    """Add the 'The quick brown fox jumps over the lazy dog' to linked list"""
    lst = Queue()

    lst.enqueue("first")
    lst.enqueue("second")
    lst.enqueue("third")
    lst.enqueue("fourth")

    assert lst.dequeue() == "first"
    assert lst.dequeue() == "second"
    assert lst.dequeue() == "third"
    assert lst.dequeue() == "fourth"


def test_empty_dequeue():
    """Test that list raises error if pop or popleft are called"""
    lst = Queue()
    with pytest.raises(TypeError):
        lst.dequeue()

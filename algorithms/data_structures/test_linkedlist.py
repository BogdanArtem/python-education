"""Linked list tests"""

import pytest
from linked_list import LinkedList


def test_pop_append():
    lst = LinkedList()

    lst.append("first")
    lst.append("second")
    lst.append("third")
    lst.append("fourth")

    assert lst.pop() == "fourth"
    assert lst.pop() == "third"
    assert lst.pop() == "second"
    assert lst.pop() == "first"

def test_prepend_popleft():
    lst = LinkedList()

    lst.prepend("first")
    lst.prepend("second")
    lst.prepend("third")
    lst.prepend("fourth")

    assert lst.popleft() == "fourth"
    assert lst.popleft() == "third"
    assert lst.popleft() == "second"
    assert lst.popleft() == "first"


def test_append_popleft():
    """Add the 'The quick brown fox jumps over the lazy dog' to linked list"""
    lst = LinkedList()

    lst.append("first")
    lst.append("second")
    lst.append("third")
    lst.append("fourth")

    assert lst.popleft() == "first"
    assert lst.popleft() == "second"
    assert lst.popleft() == "third"
    assert lst.popleft() == "fourth"


def test_delete_empty():
    """Test that list raises error if pop or popleft are called"""
    lst = LinkedList()
    with pytest.raises(IndexError):
        lst.popleft()

    with pytest.raises(IndexError):
        lst.pop()

def test_iter():
    """Test iterator of linked list"""
    lst = LinkedList()
    words = ["just", "another", "test", "to", "complete"]
    for word in words:
        lst.append(word)

    for word, node in zip(words, lst):
        assert word == node.data

    # Empty list iteration
    lst2 = LinkedList()
    for node in lst2:
        print(node.data)

def test_delete():
    """Check revoval of items from linked list"""
    lst = LinkedList()
    words = ["just", "another", "test", "to", "complete"]
    for word in words:
        lst.append(word)

    # delete in the middle
    words.remove("test")
    lst.delete(2)

    for word, node in zip(words, lst):
        print(f"After 'test' removal: {node.data}")
        assert word == node.data

    # delete at the beginnig
    words.remove("complete")
    lst.delete(3)

    for word, node in zip(words, lst):
        print(f"After 'complete' removal: {node.data}")
        assert word == node.data

    # delete at the end
    words.remove("just")
    lst.delete(0)

    for word, node in zip(words, lst):
        print(f"After 'just' removal: {node.data}")
        assert word == node.data

    # delete the only element
    lst2 = LinkedList()
    lst2.append("just a value")
    lst2.delete(0)
    assert lst2.head is None
    assert lst2.tail is None

    # delete non-existent element
    with pytest.raises(IndexError):
        lst2.delete(100)

def test_contains():
    """Check if search works"""
    lst = LinkedList()

    lst.append(5)
    lst.append(3)
    lst.append(10)
    lst.append(100)

    assert 5 in lst
    assert 1 not in lst
    assert 100 in lst

def test_lookup():
    """Check finding values by index"""
    lst = LinkedList()
    lst.append(5)
    lst.append(3)
    lst.append(10)

    assert lst.lookup(0) == 5
    assert lst.lookup(2) == 10


def test_insert():
    lst = LinkedList()
    lst.append(5)
    lst.append(3)
    lst.append(10)
    lst.append(100)
    lst.insert(0, 1)
    lst.insert(2, 17)

    assert lst.lookup(0) == 1
    assert lst.lookup(2) == 17
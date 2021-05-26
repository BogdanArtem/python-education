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

    lst.append_tail("first")
    lst.append_tail("second")
    lst.append_tail("third")
    lst.append_tail("fourth")

    assert lst.pop_tail() == "fourth"
    assert lst.pop_tail() == "third"
    assert lst.pop_tail() == "second"
    assert lst.pop_tail() == "first"


def test_linked_list_append_popleft():
    """Add the 'The quick brown fox jumps over the lazy dog' to linked list"""
    lst = LinkedList()

    lst.append("first")
    lst.append("second")
    lst.append("third")
    lst.append("fourth")

    assert lst.pop_tail() == "first"
    assert lst.pop_tail() == "second"
    assert lst.pop_tail() == "third"
    assert lst.pop_tail() == "fourth"


def test_linked_list_remove_empty():
    """Test that list raises error if pop or popleft are called"""
    lst = LinkedList()
    with pytest.raises(TypeError):
        lst.pop_tail()

    with pytest.raises(TypeError):
        lst.pop()

def test_linked_list_iter():
    """Test iterator of linked list"""
    lst = LinkedList()
    words = ["just", "another", "test", "to", "complete"]
    for word in words:
        lst.append(word)

    words.reverse()
    for word, node in zip(words, lst):
        assert word == node.data

def test_linked_list_removal():
    """Check revoval of items from linked list"""
    lst = LinkedList()
    words = ["just", "another", "test", "to", "complete"]
    for word in words:
        lst.append(word)

    # remove in the middle
    words.remove("test")
    lst.remove("test")

    words.reverse()
    for word, node in zip(words, lst):
        print(f"After 'test' removal: {node.data}")
        assert word == node.data
        
    # remove at the beginnig
    words.remove("complete")
    lst.remove("complete")

    for word, node in zip(words, lst):
        print(f"After 'complete' removal: {node.data}")
        assert word == node.data

    # remove at the end
    words.remove("just")
    lst.remove("just")

    for word, node in zip(words, lst):
        print(f"After 'just' removal: {node.data}")
        assert word == node.data
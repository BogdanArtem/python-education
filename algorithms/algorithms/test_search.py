"""Testing of binary search"""

from search import binary_search

def test_binary_search():
    """Binary search on sequences of different types"""
    arr = [1, 3, 5, 7]
    assert binary_search(arr, 7) == 7
    assert binary_search(arr, 1) == 1
    assert binary_search(arr, 100) is None

    arr1 = [1, 10]
    assert binary_search(arr1, 1) == 1
    assert binary_search(arr1, 10) == 10

    arr2 = ["a", "b", "c", "d", "e"]
    assert binary_search(arr2, "a") == "a"
    assert binary_search(arr2, "e") == "e"
    assert binary_search(arr2, "b") == "b"

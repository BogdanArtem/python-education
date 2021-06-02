"""Module for quicksort testing"""

from sort import quick_sort

def test_sort():
    """Simple test"""
    arr1 = [5, -10 , 50, 2, 0, 11]
    arr2 = [0, 0, 0, 1]
    arr3 = [-100, 0, 100]
    assert quick_sort(arr1.copy()) == sorted(arr1.copy())
    assert quick_sort(arr2.copy()) == sorted(arr2.copy())
    assert quick_sort(arr3.copy()) == sorted(arr3.copy())

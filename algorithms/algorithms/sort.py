"""Module to practice quicksort implementation"""

from typing import Any, Sequence

def quick_sort(seq: Sequence[Any]):
    """Sort values inside sequence object.

    This agorithm assumes that sequence items are comparable

    sequence: Sequence
        Object that implements Sequence methods

     """
    if not seq:
        return seq
    pivot = seq.pop()
    left = [x for x in seq if x < pivot]
    right = [x for x in seq if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

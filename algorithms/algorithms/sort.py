from typing import Any, Sequence
from random import choice

def quick_sort(seq: Sequence[Any]):
    """Sort values inside sequence object.

    This agorithm assumes that sequence items are comparable

    sequence: Sequence
        Obect that implements Sequence methods

     """
    if not seq:
        return seq
    pivot = seq.pop()
    left = [x for x in seq if x < pivot]
    right = [x for x in seq if x >= pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
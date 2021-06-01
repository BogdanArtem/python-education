"""Module to practice quicksort implementation"""


from typing import Any, Sequence


def quick_sort_iter(seq: Sequence[Any]):
    """Sort values inside sequence object.

    This algorithm assumes that sequence items are comparable

    seq: Sequence
        Object that implements Sequence methods

     """

    def partition(seq: Sequence, left: int, right: int):
        """Pivot sorting of array in range of left and right.

        Choose pivot and rearrange smaller elements in sequence to the left from pivot.

        seq: Sequence
            Object that implements Sequence methods
        left: int
            Index of the leftmost element
        right: int
            Index of the rightmost element
        return: int
            Index of the pivot
        """
        pivot_idx = left
        for i in range(left + 1, right + 1):
            if seq[i] <= seq[left]:
                pivot_idx += 1
                seq[i], seq[pivot_idx] = seq[pivot_idx], seq[i]
        seq[pivot_idx], seq[left] = seq[left], seq[pivot_idx]
        return pivot_idx

    left = 0
    right = len(seq) - 1
    stack = []
    stack.append((left, right))

    while stack:
        left, right = stack.pop()
        if left < right:
            pivot_idx = partition(seq, left, right)
            stack.append((left, pivot_idx - 1))
            stack.append((pivot_idx + 1, right))
    return seq

"""Module that implements binary search"""


from typing import Any, Sequence


def binary_search(seq: Sequence, value: Any):
    """Find value inside sequence object.

    This agorithm assumes that sequence is sorted and items are comparable

    sequence: Sequence
        Obect that implements Sequence methods

    value: Any
        Any type of value

     """

    pointer_left = 0
    pointer_right = len(seq)

    while True:
        # Find middle index
        middle = (pointer_left + pointer_right)//2
        if value == seq[middle]:
            return value
        if value < seq[middle]:
            # Exit condition if 2 pointers are together
            if pointer_right - pointer_left == 1:
                break
            # Remove right half of sequence
            pointer_right = middle
        elif value > seq[middle]:
            # Exit condition if 2 pointers are together
            if pointer_right - pointer_left == 1:
                break
            # Remove left half of sequence
            pointer_left = middle

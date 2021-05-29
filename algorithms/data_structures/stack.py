"""Implementation of stack

This module is created to practice stack implementation"""


from linked_list import LinkedList


class Stack:
    """Linked list stack implementation"""
    def __init__(self):
        self.data = LinkedList()

    def push(self, value):
        """Add values to stack"""
        self.data.append(value)

    def pop(self):
        """Remove and return values according to FILO"""
        return self.data.pop()

    def peek(self):
        """Return the last value according to FILO"""
        return self.data.tail.data

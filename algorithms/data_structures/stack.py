"""Implementation of stack

This module is created to practice stack implementation"""


from linked_list import LinkedList


class Stack:
    def __init__(self):
        self.data = LinkedList()

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()
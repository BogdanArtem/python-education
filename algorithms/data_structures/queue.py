"""Implementation of queue

This module is created to practice queue implementation"""


from linked_list import LinkedList


class Queue:
    """Queue based on linked list"""
    def __init__(self):
        self.data = LinkedList()

    def enqueue(self, value):
        """Add element to queue"""
        self.data.append(value)

    def dequeue(self):
        """Remove element according to FIFO"""
        return self.data.pop_tail()

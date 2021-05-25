"""Implementation of linked list

This module is created to practice data structures"""


class Node:
    """Node used in linked list"""
    def __init__(self, data, next_node):
        self._next = next_node
        self._data = data

    @property
    def next(self):
        """Find next node"""
        return self._next

    @next.setter
    def next(self, value):
        """Change next node"""
        self._next = value

    @property
    def data(self):
        """Get data from node"""
        return self._data

    @data.setter
    def data(self, value):
        """Change data in node"""
        return self._data


class LinkedList:
    """Simple linked list with head and tail"""
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Add node to the head of the list"""
        if self.head and self.tail is None:
            new_node = Node(value, self.head)
            self.head = new_node
            self.tail = new_node
        else:
            self.head = Node(value, self.head)

    def prepend(self, value):
        """Add node to the tail of the list"""
        if self.head and self.tail is None:
            new_node = Node(value, self.head)
            self.head = new_node
            self.tail = new_node
        else:
            self.tail = Node(value, self.tail)

    def pop(self):
        """Remove and return node from the head of the list"""
        if self.head is None:
            raise TypeError("Inappropriate operation applied to empty list")
        result = self.head.data
        self.head = self.head.next
        return result


    def popleft(self):
        """Remove and return node from the tail of the list"""
        if self.tail is None:
            raise TypeError("Inappropriate operation applied empty list")
        result = self.tail.data
        self.tail = self.tail.next
        return result

if __name__ == "__main__":
    pass

"""Implementation of linked list

This module is created to practice data structures"""


class Node:
    """Node used in linked list"""
    def __init__(self, data, next_node, previous_node):
        self._next = next_node
        self._previous = previous_node
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
    def previous(self):
        """Find next node"""
        return self._previous

    @previous.setter
    def previous(self, value):
        """Change next node"""
        self._previous = value

    @property
    def data(self):
        """Get data from node"""
        return self._data

    @data.setter
    def data(self, value):
        """Change data in node"""
        self._data = value


class LinkedList:
    """Double linked list with head and tail

    TAIL | == | == | == | == | HEAD
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.empty = True

    def __iter__(self):
        self.last_node = self.head
        return self

    def __next__(self):
        if self.last_node.data is None:
            raise StopIteration
        value = self.last_node.data
        self.last_node = self.last_node.previous
        return value

    def _add_first_node(self, value):
        """Initial setup for the first node"""
        first_node = Node(value, next_node=None, previous_node=None)
        self.head = first_node
        self.tail = first_node
        self.empty = False

    def append(self, value):
        """Add node to the head of the list"""
        if not self.empty:
            # Create new head node making link to the previous head node
            new_head_node = Node(value, next_node=None, previous_node=self.head)
            # Make link to the new head node from old head node
            self.head.next = new_head_node
            # Set new head of list
            self.head = new_head_node
        else:
            self._add_first_node(value)

    def append_tail(self, value):
        """Add node to the tail of the list"""
        if not self.empty:
            # Create new tail node making link to the current tail node
            new_tail_node = Node(value, next_node=self.tail, previous_node=None)
            # Make link to the new tail node from old tail node
            self.tail.previous = new_tail_node
            # Set new tail of list
            self.tail = new_tail_node
        else:
            self._add_first_node(value)

    def pop(self):
        """Remove node from head and return it's data"""
        if self.head is None:
            raise TypeError("Inappropriate operation applied to empty list")
        result = self.head.data
        self.head = self.head.previous
        return result

    def pop_tail(self):
        """Remove node from tail and return it's data"""
        if self.tail is None:
            raise TypeError("Inappropriate operation applied empty list")
        result = self.tail.data
        self.tail = self.tail.next
        return result

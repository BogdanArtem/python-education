"""Implementation of double linked list

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

    Iteration is performed from HEAD to TAIL

    HEAD | == | == | == | == | TAIL
    """
    def __init__(self):
        self.head = None
        self.tail = None
        self.empty = True

    def __iter__(self):
        self.node_memo = self.head
        return self

    def __contains__(self, value):
        for node in self:
            if node.data == value:
                return True
        return False

    def __repr__(self):
        result = ", ".join((str(node.data) for node in self))
        return "<" + result + ">"

    def __next__(self):
        """Travese list nodes from TAIL to HEAD"""
        if self.node_memo is None:
            raise StopIteration
        value = self.node_memo
        self.node_memo = self.node_memo.next
        return value

    def _add_first_node(self, value):
        """Initial setup for the first node"""
        first_node = Node(value, next_node=None, previous_node=None)
        self.head = first_node
        self.tail = first_node
        self.empty = False

    def prepend(self, value):
        """Add node to the head of the list"""
        if not self.empty:
            # Create new head node making link to the previous head node
            new_head_node = Node(value, next_node=self.head, previous_node=None)
            # Make link to the new head node from old head node
            self.head.previous = new_head_node
            # Set new head of list
            self.head = new_head_node
        else:
            self._add_first_node(value)

    def append(self, value):
        """Add node to the tail of the list"""
        if not self.empty:
            # Create new tail node making link to the current tail node
            new_tail_node = Node(value, next_node=None, previous_node=self.tail)
            # Make link to the new tail node from old tail node
            self.tail.next = new_tail_node
            # Set new tail of list
            self.tail = new_tail_node
        else:
            self._add_first_node(value)

    def popleft(self):
        """Remove node from tail and return it's data"""
        if self.head is None:
            raise IndexError("Inappropriate operation applied to empty list")
        result = self.head.data
        self.head = self.head.next
        return result

    def pop(self):
        """Remove node from tail and return it's data"""
        if self.tail is None:
            raise IndexError("Inappropriate operation applied empty list")
        result = self.tail.data
        self.tail = self.tail.previous
        return result

    def insert(self, index, value):
        """Insert value in place of index and shit other values to the right"""
        for node_index, node in enumerate(self):
            if index  == node_index:
                # Access the previous node of index node
                previous_node = node.previous
                # Set links of new node to previous node and to index node
                new_node = Node(value, next_node=node, previous_node=previous_node)
                # Set next node of previous node to new node
                if previous_node: # Check for None
                    previous_node.next = new_node
                else:
                    self.head = new_node

                # Set previous node of index node to new node
                node.previous = new_node

    def lookup(self, index):
        """Find value by index"""
        for node_index, node in enumerate(self):
            if node_index == index:
                return node.data

    def delete(self, index):
        """Traverse values in linked list
        HEAD to TAIL and delete the fist
        node that matches index"""
        for node_index, node in enumerate(self):
            if node_index == index:
                # Get reference to previous and next nodes
                previous = node.previous
                _next = node.next
                # Make them reference each other
                if previous is None:
                    # Change head reference if head is removed
                    self.head = _next
                else:
                    previous.next = _next
                if _next is None:
                    # Change head reference if head is removed
                    self.tail = previous
                else:
                    _next.previous = previous
                return None
        raise IndexError

"""Implementation of binary search tree

This module is created to practice hash table implementation"""


from array import Array
from linked_list import LinkedList


class HashTable:
    """Hash table based on Array and LinkedList"""
    def __init__(self, size):
        self.size = size
        self.table = self._create_table()

    def _create_table(self):
        """Create Array filled with LinkedList"""
        table = Array(self.size)
        for i in range(self.size):
            table[i] = LinkedList()
        return table

    def __contains__(self, value):
        """Check if value is in table"""
        cell = self._get_cell(value)
        for node in cell:
            if value == node.data:
                return True
        return False

    def _get_index(self, value):
        return self._hash(value) % self.size

    def _hash(self, value):
        """Return hash value of hashable object"""
        return hash(value)

    def _get_cell(self, value):
        """Return cell of Array containing LinkedList"""
        index = self._get_index(value)
        return self.table[index]

    def insert(self, value):
        """Incert value into linked list"""
        cell = self._get_cell(value)
        cell.append(value)

    def delete(self, value):
        """Delete value from linked list"""
        cell = self._get_cell(value)
        cell.remove(value)
        
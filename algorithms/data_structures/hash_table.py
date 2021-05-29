"""Implementation of binary search tree

This module is created to practice hash table implementation"""


from array import Array
from linked_list import LinkedList


class KeyValue:
    def __init__(self, key, value):
        self._key = key
        self._value = value

    @property
    def key(self):
        return self._key

    @property
    def value(self):
        return self._value

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

    def __contains__(self, key):
        """Check if key is in table"""
        cell = self._get_cell(value)
        for node in cell:
            if value == node.data:
                return True
        return False

    def _get_index(self, key):
        """"""
        return self._hash(key) % self.size

    def _hash(self, value):
        """Return hash value of hashable object"""
        return hash(value)

    def _get_cell(self, key):
        """Return cell of Array containing LinkedList"""
        index = self._get_index(key)
        return self.table[index]

    # Done
    def insert(self, key, value):
        """Incert value into linked list"""
        cell = self._get_cell(key)
        key_value = KeyValue(key, value)
        cell.append(key_value)

    def lookup(self, key):
        cell = self._get_cell(key)
        for node in cell:
            key_value = node.data
            if key_value.key == key:
                return key_value.value

    def delete(self, key):
        """Delete value from linked list.
        
        Raise KeyError if key does not exist
        """
        cell = self._get_cell(key)
        for index, node in enumerate(cell):
            key_value = node.data
            if key_value.key == key:
                cell.delete(index)
                return None
        raise KeyError

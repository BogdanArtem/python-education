"""Implementation of binary search tree

This module is created to practice graph implementation as adjacency list"""


from dynamic_array import DynamicArray
from linked_list import LinkedList


class Graph:
    """Adjacency list implementation of directed graph with values storage"""
    def __init__(self, size):
        self.connections = DynamicArray(size)
        self.values = DynamicArray(size)

    def add_node(self, node_idx, value):
        """Add node using array index"""
        if not self._valid_index(node_idx):
            raise IndexError("Index does not exis")
        if self.values[node_idx] is None:
            self.connections[node_idx] = LinkedList()
            self.values[node_idx] = value
        else:
            raise ValueError("Node is already present at this index")

    def delete_node(self, node_idx):
        """Remove node and all connections to it"""
        if not self._valid_index(node_idx):
            raise IndexError("Index does not exis")
        if self.values[node_idx] is None:
            raise ValueError("Node does not exist")

        self.connections[node_idx] = None
        self.values[node_idx] = None
        # Delete all connections to node
        for node in self.connections:
            if node is not None and node_idx in node:
                node.remove(node_idx)

    def add_connection(self, index_1, index_2):
        """Create directed connection between nodes of graph"""
        if not self._valid_index(index_1, index_2):
            raise IndexError("Index does not exis")
        if self.has_connection(index_1, index_2):
            raise ValueError("Connection already exists")
        node = self.connections[index_1]
        node.append(index_2)

    def remove_connection(self, index_1, index_2):
        """Remove directed connection between two nodes"""
        if not self.has_connection(index_1, index_2):
            raise ValueError("Connection does not exist")
        node = self.connections[index_1]
        node.remove(index_2)

    def has_directed_connection(self, index_1, index_2):
        """Check if node index1 has directed connection to index2"""
        if not self._valid_index(index_1, index_2):
            raise IndexError("Index does not exits")
        node = self.connections[index_1]
        # Check if node exists
        return True if node and index_2 in node else False

    def has_connection(self, index_1, index_2):
        """Check is 2 contiguous nodes have connctions in 2 directions"""
        if not self._valid_index(index_1, index_2):
            raise IndexError("Index does not exis")
        return self.has_directed_connection(index_1, index_2) or \
            self.has_directed_connection(index_2, index_1)

    def _valid_index(self, *args: int):
        """Check if index exists in array"""
        for index in args:
            if not self._node_exists(index):
                return False
        return True

    def _node_exists(self, index):
        """Check if index corresponds to node"""
        try:
            self.connections[index]
            self.values[index]
            return True
        except IndexError:
            return False

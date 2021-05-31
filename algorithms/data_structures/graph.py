"""Implementation of binary search tree

This module is created to practice graph implementation as adjacency list"""


from linked_list import LinkedList


class Graph:
    """Adjacency list implementation of directed graph
    
    Linked list represents graph of nodes. Edges are represented as
    linked list of nodes indexes, connected to node.
    """
    def __init__(self):
        self.nodes = LinkedList()

    def __repr__(self):
        return "Graph" + repr(self.nodes)

    def insert(self, *links: int):
        """Add node with links """
        edges = LinkedList()
        for link in links:
            edges.append(link)
        self.nodes.append(edges)

    def lookup(self, node_index: int):
        """Return node using value"""
        return self.nodes.lookup(node_index)

    def delete(self, node_index: int):
        """Delete node and its references to other nodes"""

        # Delete references from other nodes
        for node in self.nodes:
            for index, link in enumerate(node.data):
                if link.data == node_index:
                    node.data.delete(index)

        # Delete node and its references
        self.nodes.delete(node_index)

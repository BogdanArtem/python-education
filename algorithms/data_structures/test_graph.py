"""Graph tests"""

import pytest
from graph import Graph

@pytest.fixture
def graph():
    """
    Graph schema

        2 ---  4
      /  \   /
    1 ---  3

    """
    graph = Graph(5)

    graph.add_node(node_idx = 1, value = 45)
    graph.add_node(node_idx = 2, value = 30)
    graph.add_node(node_idx = 3, value = 2)
    graph.add_node(node_idx = 4, value = 70)

    graph.add_connection(1, 2)
    graph.add_connection(1, 3)
    graph.add_connection(2, 3)
    graph.add_connection(2, 4)
    graph.add_connection(4, 3)

    return graph

def test_connections(graph):
    """Check the presence of connections"""
    assert graph.has_connection(2, 3) is True
    assert graph.has_connection(3, 2) is True
    assert graph.has_directed_connection(2, 3) is True
    assert graph.has_directed_connection(3, 2) is False

    assert graph.has_connection(3, 4) is True
    assert graph.has_connection(4, 3) is True
    assert graph.has_directed_connection(4, 3) is True
    assert graph.has_directed_connection(3, 4) is False

    assert graph.has_connection(1, 2) is True
    assert graph.has_connection(2, 1) is True

    assert graph.has_connection(2, 4) is True
    assert graph.has_connection(4, 2) is True

    assert graph.has_connection(1, 3) is True
    assert graph.has_connection(3, 1) is True

    assert graph.has_connection(1, 4) is False
    assert graph.has_connection(4, 1) is False

def test_connections_removal(graph):
    """Check if nodes with connections are removed"""
    graph.remove_connection(2, 3)
    assert graph.has_connection(3, 2) is False

    graph.remove_connection(4, 3)

    assert graph.has_connection(1, 2) is True
    assert graph.has_connection(2, 4) is True

def test_nodes_removal(graph):
    """Check if nodes are removed"""
    graph.delete_node(3)

    assert graph.has_connection(2, 1) is True
    assert graph.has_connection(2, 4) is True
    assert graph.has_connection(1, 3) is False
    assert graph.has_connection(3, 4) is False
    assert graph.has_connection(1, 4) is False

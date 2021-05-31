"""Graph tests"""

import pytest
from graph import Graph

@pytest.fixture
def graph():
    """
    Graph schema

        1 ---  3
      /  \   /
    0 ---  2

    """
    graph = Graph()
    graph.insert(1, 2)
    graph.insert(0, 2, 3)
    graph.insert(0, 1, 3)
    graph.insert(1, 2)
    return graph

def test_lookup(graph):
    """Check the presence of connections"""
    node1 = graph.lookup(0)
    assert str(node1) == "<1, 2>"

    node2 = graph.lookup(3)
    assert str(node2) == "<1, 2>"

    node3 = graph.lookup(1)
    assert str(node3) == "<0, 2, 3>"

def test_insert(graph):
    # Insert graph with connections to 0 and 2
    graph.insert(0, 2)
    node = graph.lookup(4)
    assert str(node) == "<0, 2>"

def test_delete0(graph):
    """Graph<<1, 2>, <0, 2, 3>, <0, 1, 3>, <1, 2>>"""
    graph.delete(0)
    print(graph)
    assert str(graph) == "Graph<<2, 3>, <1, 3>, <1, 2>>"

def test_delete1(graph):
    """Graph<<1, 2>, <0, 2, 3>, <0, 1, 3>, <1, 2>>"""
    graph.delete(1)
    print(graph)
    assert str(graph) == "Graph<<2>, <0, 3>, <2>>"

def test_delete2(graph):
    """Graph<<1, 2>, <0, 2, 3>, <0, 1, 3>, <1, 2>>"""
    graph.delete(2)
    print(graph)
    assert str(graph) == "Graph<<1>, <0, 3>, <1>>"


def test_delete3(graph):
    """Graph<<1, 2>, <0, 2, 3>, <0, 1, 3>, <1, 2>>"""
    graph.delete(3)
    print(graph)
    assert str(graph) == "Graph<<1, 2>, <0, 2>, <0, 1>>"

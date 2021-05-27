"""Binary tree tests"""


import pytest
from binary_tree import BinaryTree


@pytest.fixture
def tree():
    """
    Representation of tree

             5
           /   \
         2      10
        /       / \
       1       6   12
                   /\
                 11   15

    """
    new_tree = BinaryTree(5)
    new_tree.insert(10)
    new_tree.insert(12)
    new_tree.insert(2)
    new_tree.insert(6)
    new_tree.insert(11)
    new_tree.insert(1)
    new_tree.insert(15)
    return new_tree


def test_find_node(tree):
    """Check finding nodes in binary tree"""
    node1 = tree.find_node(1)
    assert node1.value == 1

    node2 = tree.find_node(10)
    assert node2.value == 10

    node2 = tree.find_node(2)
    assert node2.value == 2

    node2 = tree.find_node(5)
    assert node2.value == 5

    node2 = tree.find_node(1)
    assert node2.value == 1

    with pytest.raises(ValueError):
        tree.find_node(1000)


def test_delete_value(tree):
    """Check deleting values"""
    # Delete node with 2 references
    tree.delete(12)

    with pytest.raises(ValueError):
        tree.find_node(12)

    # Check referenced nodes
    node1 = tree.find_node(11)
    node2 = tree.find_node(15)

    assert node1.value == 11
    assert node2.value == 15

    # Delete node with 1 referecne
    tree.delete(2)

    with pytest.raises(ValueError):
        tree.find_node(2)

    # Check referenced node
    tree.find_node(1)

    # Delete end node
    tree.delete(6)

    with pytest.raises(ValueError):
        tree.find_node(6)

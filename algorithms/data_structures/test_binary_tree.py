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


def test_lookup(tree):
    """Check finding nodes in binary tree"""
    node1 = tree.lookup(5)
    assert node1.value == 5
    assert node1.left.value == 2
    assert node1.right.value == 10

    node2 = tree.lookup(1)
    assert node2.value == 1
    assert node2.left == None
    assert node2.right == None

    node3 = tree.lookup(10)
    assert node3.value == 10
    assert node3.left.value == 6
    assert node3.right.value == 12

    node4 = tree.lookup(12)
    assert node4.value == 12
    assert node4.left.value == 11
    assert node4.right.value == 15

    node5 = tree.lookup(11)
    assert node5.value == 11
    assert node5.left == None
    assert node5.right == None

    node6 = tree.lookup(15)
    assert node6.value == 15
    assert node6.left == None
    assert node6.right == None

    with pytest.raises(ValueError):
        tree.lookup(1000)


def test_delete(tree):
    """Check deleting values
    Before 

             5
           /   \
         2      10
        /       / \
       1       6   12
                   /\
                 11   15
    After 

             5
           /   \
         2      10
        /       / \
       1       6   11
                    \
                     15
    
    """
    # Delete node with 2 references
    tree.delete(12)

    with pytest.raises(ValueError):
        tree.lookup(12)

    # Check nodes after deletion
    node1 = tree.lookup(10)
    assert node1.value == 10
    assert node1.left.value == 6
    assert node1.right.value == 11

    node2 = tree.lookup(11)
    assert node2.value == 11
    assert node2.left == None
    assert node2.right.value == 15

    node3 = tree.lookup(15)
    assert node3.value == 15
    assert node3.left == None
    assert node3.right == None

    """
    Before 

             5
           /   \
         2      10
        /       / \
       1       6   11
                    \
                     15
    
    After
             5
           /   \
         1      10
                / \
               6   11
                    \
                     15
    
    """

    # Delete node with 1 referecne
    tree.delete(2)

    with pytest.raises(ValueError):
        tree.lookup(2)

    # Check referenced node
    node4 = tree.lookup(1)
    assert node4.value == 1
    assert node4.left == None
    assert node4.right == None

    node5 = tree.lookup(5)
    assert node5.left.value == 1
    assert node5.right.value == 10

    """
    Before
             5
           /   \
         1      10
                / \
               6   11
                    \
                     15
    After
             5
           /   \
         1      10
                  \
                   11
                    \
                     15

    """

    # Delete end node
    tree.delete(6)

    with pytest.raises(ValueError):
        tree.lookup(6)

    node6 = tree.lookup(10)
    assert node6.value == 10
    assert node6.left == None
    assert node6.right.value == 11
    
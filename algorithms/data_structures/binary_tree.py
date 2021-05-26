"""Implementation of binary search tree

This module is created to practice binary search tree implementation"""


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.count = 1
        self.left = None
        self.right = None

    def _traverse_tree(self, side, match, value):
        if self.value < value:
            return side('right', value)
        elif self.value > value:
            return side('left', value)
        elif self.value == value:
            return match()
        else:
            raise ValueError("Can't compare to value")        

    def insert(self, value):
        """Insert node with value into tree"""
        self._traverse_tree(
            side = self._add_to_the_side, 
            match = self._insert_match, 
            value = value)

    def find_node(self, value):
        """Return node that corresponds to the value"""
        return self._traverse_tree(
            side = self._find_on_the_side, 
            match = self._find_match, 
            value = value)

    def delete(self, value):
        """Remove element from tree"""
        self._traverse_tree(
            side = self._delete_on_the_side, 
            match = self._delete_match, 
            value = value)

    def _add_to_the_side(self, side: str, value):
        """Add to the left of right"""
        side_node = getattr(self, side)
        if side_node is None:
            setattr(self, side, BinaryTree(value))
        else:
            side_node.insert(value)

    def _find_on_the_side(self, side, value):
        side_node = getattr(self, side)
        if side_node is None:
            raise ValueError("Can't find the element")
        else:
            return side_node.find_node(value)

    def _delete_on_the_side(self, side, value):
        side_node = getattr(self, side)
        # Check if the last node with matching value, if so, delete it
        if side_node.left is None and side_node.right is None:
            if side_node.value == value:
                setattr(self, side, None)

        if side_node is None:
            raise ValueError("Can't delete absent node")
        else:
            return side_node.delete(value)
        

    def _insert_match(self):
        self.count += 1
    
    def _find_match(self):
        return self
        
    def _delete_match(self):
        if self.left is not None:
            self.value = self.left.value
            self.count = self.left.count
            self.left = None
        elif self.right is not None:
            self.value = self.right.value
            self.count = self.right.count
            self.right = None
        else: 
            pass

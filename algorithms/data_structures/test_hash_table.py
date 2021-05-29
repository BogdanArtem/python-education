"""HashTable tests"""

import pytest
from hash_table import HashTable

def test_hash_table():
    """Check inserition and deletion"""
    table = HashTable(10)

    table.insert('Alex', 3545)
    table.insert('Sam', 1000)
    table.insert('John', 1999)
    table.insert('Max', 9999)
    table.insert('Nick', 0)

    assert table.lookup("John") == 1999
    assert table.lookup("Max") == 9999

    table.delete('Nick')
    assert table.lookup("Nick") == None

    with pytest.raises(KeyError):
        table.delete('Nick')
    
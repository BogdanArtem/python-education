"""HashTable tests"""

import pytest
from hash_table import HashTable

def test_hash_table():
    table = HashTable(10)

    table.insert('just')
    table.insert('another')
    table.insert('test')

    assert "just" in table
    table.delete('just')
    assert "just" not in table 

    with pytest.raises(ValueError):
        table.delete('just')
    
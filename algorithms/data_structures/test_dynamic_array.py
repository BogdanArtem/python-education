"""Binary tree tests"""


from dynamic_array import DynamicArray


def test_dynamic_array():
    """Test methods of array"""
    arr = DynamicArray(3)

    arr[0] = "this"
    arr[1] = "is"
    arr[2] = "just"
    arr[3] = "another"
    arr[4] = "test"
    arr[5] = "!"

    assert arr.num_items == 6
    assert arr.size == 12

    arr[0] = None
    assert arr.num_items == 5

    arr[1] = "text"
    assert arr.num_items == 5

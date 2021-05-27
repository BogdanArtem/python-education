"""Testing of factorial"""


from factorial import factorial


def test_factorial():
    """Simple factorial test"""
    assert factorial(0) == 0
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6

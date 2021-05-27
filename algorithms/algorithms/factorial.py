"Module that implements factorial recursive function"

def factorial(num: int):
    """Find factorial of n.

    This algorithm uses recursion to find factorial of n

    n: int
        number to find factorial

    """

    if num in (1, 0):
        return num
    return num * factorial(num - 1)

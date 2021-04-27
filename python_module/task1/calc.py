"""This is a module for mathematical operations"""

class Calculator:
    """Class for basic mathematical operations"""

    @staticmethod
    def add(arg1, arg2):
        """Add arg1 and arg2"""
        return arg1 + arg2

    @staticmethod
    def subtract(arg1, arg2):
        """Subtract arg2 from arg1"""
        return arg1 - arg2

    @staticmethod
    def multiply(arg1, arg2):
        """Multiply arg1 by arg2"""
        return arg1 * arg2

    @staticmethod
    def divide(arg1 , arg2):
        """Divide arg1 by arg2"""
        return arg1/arg2


if __name__ == "__main__":
    #Tests
    print(f"5 + 10 = {Calculator.add(5, 10)}")
    print(f"5 - 10 = {Calculator.subtract(5, 10)}")
    print(f"5 * 10 = {Calculator.multiply(5, 10)}")
    print(f"5 / 10 = {Calculator.divide(5, 10)}")

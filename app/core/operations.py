"""
Defines basic arithmetic functions that can be used independently of the object-oriented command structure.
"""

def add(a, b):
    """
    Returns the sum of two numbers.

    :param a: First operand.
    :param b: Second operand.
    :return: Sum of a and b.
    """
    return a + b

def subtract(a, b):
    """
    Returns the result of subtracting b from a.

    :param a: Minuend.
    :param b: Subtrahend.
    :return: Difference of a and b.
    """
    return a - b

def multiply(a, b):
    """
    Returns the product of two numbers.

    :param a: First operand.
    :param b: Second operand.
    :return: Product of a and b.
    """
    return a * b

def divide(a, b):
    """
    Returns the result of dividing a by b.

    :param a: Dividend.
    :param b: Divisor.
    :return: Quotient of a divided by b.
    :raises ValueError: If b is zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

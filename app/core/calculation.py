"""
This module contains the Calculation class that models an arithmetic operation 
involving two operands and a specified command to execute the operation.
"""

from decimal import Decimal

class Calculation:
    """
    Represents a single arithmetic calculation.
    """

    def __init__(self, a: Decimal, b: Decimal, operation):
        """
        Initializes a new Calculation instance.

        :param a: First operand as a Decimal.
        :param b: Second operand as a Decimal.
        :param operation: Operation object that has an execute method.
        """
        self.a = a
        self.b = b
        self.operation = operation
        self.result = None

    def operate(self) -> Decimal:
        """
        Executes the assigned operation on the operands.

        :return: Decimal result of the operation.
        """
        self.result = self.operation.execute(self.a, self.b)
        return self.result
    
    def __str__(self) -> str:
        """
        Return a string representation of the Calculation instance.

        Returns:
            str: A string describing the calculation.
        """
        return f"Calculation({self.a}, {self.b}, {self.operation.operation_name})"


"""
This module defines the `MeanCommand` class for calculating the mean of two numbers.
"""

from decimal import Decimal
from app.core.command import Command

class MeanCommand(Command):
    """
    Command class for calculating the mean (average) of two numbers.
    """

    operation_name = "mean"

    def execute(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Computes the arithmetic mean of two numbers.

        Args:
            num1 (Decimal): First number.
            num2 (Decimal): Second number.

        Returns:
            Decimal: The mean of num1 and num2.
        """
        return (num1 + num2) / Decimal(2)

    def execute_multiprocessing(self, num1: Decimal, num2: Decimal, result_queue):
        """
        Performs the mean calculation in a separate process.

        Args:
            num1 (Decimal): First number.
            num2 (Decimal): Second number.
            result_queue (multiprocessing.Queue): Queue to store the result.
        """
        result = self.execute(num1, num2)
        result_queue.put(result)

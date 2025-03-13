"""
This module defines the `MedianCommand` class for calculating the median of two numbers.
"""

from decimal import Decimal
from app.core.command import Command

class MedianCommand(Command):
    """
    Command class for calculating the median (average of two numbers).
    """

    operation_name = "median"

    def execute(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Computes the median of two numeric inputs.

        Args:
            num1 (Decimal): First number.
            num2 (Decimal): Second number.

        Returns:
            Decimal: The median of num1 and num2.
        """
        return (num1 + num2) / Decimal(2)

    def execute_multiprocessing(self, num1: Decimal, num2: Decimal, result_queue):
        """
        Executes the median calculation using multiprocessing.

        Args:
            num1 (Decimal): First number.
            num2 (Decimal): Second number.
            result_queue (multiprocessing.Queue): Queue to store the result.
        """
        result = self.execute(num1, num2)
        result_queue.put(result)

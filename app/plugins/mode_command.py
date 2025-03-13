"""
This module defines the `ModeCommand` class for finding the mode of two numbers.
"""

from decimal import Decimal
from app.core.command import Command

class ModeCommand(Command):
    """
    Command class for finding the mode between two numbers.
    """

    operation_name = "mode"

    def execute(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Returns the mode of two numbers. 
        If they are equal, returns that value (mode). 
        If different, returns the smallest one (arbitrary choice).

        Args:
            num1 (Decimal): First number.
            num2 (Decimal): Second number.

        Returns:
            Decimal: The mode or selected number.
        """
        if num1 == num2:
            return num1
        else:
            # Mode requires frequency; here we arbitrarily return the smaller number
            return min(num1, num2)

    def execute_multiprocessing(self, num1: Decimal, num2: Decimal, result_queue):
        """
        Executes the mode operation in a separate process.

        Args:
            num1 (Decimal): First number.
            num2 (Decimal): Second number.
            result_queue (multiprocessing.Queue): Queue to store the result.
        """
        result = self.execute(num1, num2)
        result_queue.put(result)

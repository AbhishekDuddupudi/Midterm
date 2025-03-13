"""
Defines the abstract Command class, serving as a blueprint for arithmetic operation commands.
"""

from decimal import Decimal
from abc import ABC, abstractmethod

class Command(ABC):
    """
    Abstract class that specifies the interface for calculator commands.
    """

    operation_name: str  # Should be overridden by subclasses

    @abstractmethod
    def execute(self, num1: Decimal, num2: Decimal) -> Decimal:
        """
        Executes the arithmetic operation.

        :param num1: First number.
        :param num2: Second number.
        :return: Result as a Decimal.
        """
        pass  # Implementation is required in subclasses

    @abstractmethod
    def execute_multiprocessing(self, num1: Decimal, num2: Decimal, result_queue):
        """
        Executes the operation in a separate process and puts the result in the queue.

        :param num1: First operand.
        :param num2: Second operand.
        :param result_queue: Multiprocessing queue to store the result.
        """
        pass  # Implementation is required in subclasses

"""
This module defines the Calculations class for managing and persisting 
a history of performed calculations, backed by Pandas.
"""

import pandas as pd
from app.core.calculation import Calculation
from app.utils.pandas_facade import PandasFacade

class Calculations:
    """
    Maintains a collection of Calculation records and provides history management utilities.
    """

    _facade = PandasFacade()

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        """
        Adds a completed calculation to the history log.

        :param calculation: The Calculation instance containing operation details.
        """
        record = {
            "operation": calculation.operation.operation_name,
            "num1": calculation.a,
            "num2": calculation.b,
            "result": calculation.result
        }
        cls._facade.add_record(record)

    @classmethod
    def clear_history(cls):
        """
        Clears all recorded calculations from the history.
        """
        cls._facade.clear()

    @classmethod
    def get_all_calculations(cls) -> pd.DataFrame:
        """
        Retrieves the entire history as a pandas DataFrame.

        :return: DataFrame containing all calculation records.
        """
        return cls._facade.dataframe

    @classmethod
    def filter_with_operation(cls, operation: str) -> pd.DataFrame:
        """
        Filters the history for records that match the provided operation.

        :param operation: Name of the operation to filter by.
        :return: Filtered DataFrame of matching records.
        """
        return cls._facade.filter_by_operation(operation)

    @classmethod
    def save_history(cls, filepath: str):
        """
        Persists the history to a CSV file at the specified location.

        :param filepath: Path where the history CSV should be stored.
        """
        cls._facade.save_to_file(filepath)

    @classmethod
    def load_history(cls, filepath: str):
        """
        Loads calculation history from a CSV file.

        :param filepath: Path of the CSV file to load.
        """
        cls._facade.load_from_file(filepath)

    @classmethod
    def delete_history(cls, index: int):
        """
        Removes a calculation from history by its index.

        :param index: Row index to delete from the DataFrame.
        """
        cls._facade.delete_record(index)

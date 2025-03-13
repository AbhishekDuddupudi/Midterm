"""
Implements a simplified interface over Pandas for manipulating calculation records stored as a DataFrame.
"""

import pandas as pd
import os

class PandasFacade:
    """
    Simplifies common Pandas DataFrame operations for managing calculation records.
    """

    def __init__(self):
        """
        Initializes an empty DataFrame with predefined columns.
        """
        self.dataframe = pd.DataFrame(columns=["operation", "num1", "num2", "result"])

    def add_record(self, record: dict):
        """
        Appends a new record to the DataFrame.

        :param record: Dictionary representing a single calculation record.
        """
        new_entry = pd.DataFrame([record])
        self.dataframe = pd.concat([self.dataframe, new_entry], ignore_index=True)

    def clear(self):
        """
        Clears all records from the DataFrame.
        """
        self.dataframe = pd.DataFrame(columns=self.dataframe.columns)

    def filter_by_operation(self, operation: str) -> pd.DataFrame:
        """
        Returns records where the operation matches the specified name.

        :param operation: Operation name to filter by.
        :return: Filtered DataFrame.
        """
        return self.dataframe[self.dataframe["operation"] == operation]

    def save_to_file(self, filepath: str):
        """
        Saves the DataFrame to a CSV file.

        :param filepath: Filepath where the CSV file will be stored.
        """
        directory = os.path.dirname(filepath)
        if directory and not os.path.exists(directory):
            os.makedirs(directory)
        self.dataframe.to_csv(filepath, index=False)

    def load_from_file(self, filepath: str):
        """
        Loads records from an existing CSV file into the DataFrame.

        :param filepath: Path to the CSV file to load.
        """
        if os.path.exists(filepath):
            self.dataframe = pd.read_csv(filepath)
        else:
            raise FileNotFoundError(f"No such file: '{filepath}'")
        
    def delete_record(self, index: int):
        """
        Delete a record from the DataFrame by its index.

        Args:
            index (int): The index of the record to delete.
        """
        if 0 <= index < len(self.dataframe):
            self.dataframe = self.dataframe.drop(index).reset_index(drop=True)
            print(f"Deleted calculation at index {index}.")
        else:
            print(f"Index {index} is out of range. Unable to delete.")  # <- FIXED MESSAGE


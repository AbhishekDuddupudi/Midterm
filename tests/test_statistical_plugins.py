import pytest
import multiprocessing
from decimal import Decimal
from multiprocessing import Queue
from app.plugins.mean_command import MeanCommand
from app.plugins.median_command import MedianCommand
from app.plugins.mode_command import ModeCommand

# -----------------------------------
# MeanCommand Tests
# -----------------------------------
def test_mean_command_execute():
    command = MeanCommand()
    result = command.execute(Decimal(10), Decimal(20))
    assert result == Decimal(15)

def test_mean_command_execute_multiprocessing():
    command = MeanCommand()
    result_queue = Queue()
    
    command.execute_multiprocessing(Decimal(10), Decimal(20), result_queue)
    result = result_queue.get()
    
    assert result == Decimal(15)

# -----------------------------------
# MedianCommand Tests
# -----------------------------------
def test_median_command_execute():
    command = MedianCommand()
    result = command.execute(Decimal(30), Decimal(10))
    assert result == Decimal(20)

def test_median_command_execute_multiprocessing():
    command = MedianCommand()
    result_queue = Queue()
    
    command.execute_multiprocessing(Decimal(30), Decimal(10), result_queue)
    result = result_queue.get()
    
    assert result == Decimal(20)

# -----------------------------------
# ModeCommand Tests
# -----------------------------------
def test_mode_command_execute_same_values():
    command = ModeCommand()
    result = command.execute(Decimal(5), Decimal(5))
    assert result == Decimal(5)

def test_mode_command_execute_different_values():
    command = ModeCommand()
    result = command.execute(Decimal(5), Decimal(10))
    # Arbitrary choice: returns the smaller of the two when no mode
    assert result == Decimal(5)

def test_mode_command_execute_multiprocessing_same_values():
    command = ModeCommand()
    result_queue = Queue()

    command.execute_multiprocessing(Decimal(7), Decimal(7), result_queue)
    result = result_queue.get()

    assert result == Decimal(7)

def test_mode_command_execute_multiprocessing_different_values():
    command = ModeCommand()
    result_queue = Queue()

    command.execute_multiprocessing(Decimal(12), Decimal(20), result_queue)
    result = result_queue.get()

    assert result == Decimal(12)  # Assuming smallest value when no clear mode

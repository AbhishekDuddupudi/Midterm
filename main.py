# Refactored REPL and Main Entry Point

import multiprocessing
import sys
import importlib
import os
import logging
from decimal import Decimal, InvalidOperation
from collections import OrderedDict
from dotenv import load_dotenv
from app.core.calculations import Calculations
from app.core.calculation import Calculation
from logger_config import configure_logging

# Load environment settings
def initialize_environment():
    load_dotenv()
    env_settings = {key: value for key, value in os.environ.items()}
    logging.info("Environment variables successfully loaded.")
    return env_settings

# Discover and load plugin commands
def discover_plugins():
    command_registry = OrderedDict()
    plugins_directory = os.path.join('app', 'plugins')

    if not os.path.exists(plugins_directory):
        logging.warning(f"Plugins directory does not exist: {plugins_directory}")
        return command_registry

    for file in os.listdir(plugins_directory):
        if file.endswith('_command.py'):
            try:
                module_name = file[:-3]
                module = importlib.import_module(f'app.plugins.{module_name}')
                command_class = getattr(module, module_name[:-8].capitalize() + 'Command')
                command_registry[module_name[:-8]] = command_class()
                logging.info(f"Plugin loaded: {module_name}")
            except (ImportError, AttributeError) as e:
                logging.error(f"Error loading plugin {module_name}: {e}")

    return command_registry

# Logging decorator for function execution
def execution_logger(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Running {func.__name__}")
        try:
            return func(*args, **kwargs)
        except Exception as err:
            logging.error(f"Error in {func.__name__}: {err}")
            raise
    return wrapper

@execution_logger
def execute_operation(num1, num2, operation_key, command_registry, multiprocess=False):
    logging.debug(f"Starting operation: {num1} {operation_key} {num2}")
    try:
        dec_num1, dec_num2 = map(Decimal, [num1, num2])
        command = command_registry.get(operation_key)

        if not command:
            logging.warning(f"Operation '{operation_key}' not found.")
            print(f"Invalid operation: {operation_key}")
            return

        if multiprocess:
            result_queue = multiprocessing.Queue()
            process = multiprocessing.Process(
                target=command.execute_multiprocessing,
                args=(dec_num1, dec_num2, result_queue)
            )
            process.start()
            process.join()

            if not result_queue.empty():
                result = result_queue.get()
                logging.info(f"Multiprocess result: {result}")
                print(f"{num1} {operation_key} {num2} (multiprocessing) = {result}")
            else:
                logging.error("Multiprocess queue returned no result.")
                print("Multiprocessing error.")
        else:
            result = command.execute(dec_num1, dec_num2)
            logging.info(f"Result: {result}")
            print(f"{num1} {operation_key} {num2} = {result}")

        calculation = Calculation(dec_num1, dec_num2, command)
        calculation.operate()
        Calculations.add_calculation(calculation)
        logging.debug("Calculation logged in history.")

    except InvalidOperation:
        logging.error(f"Invalid numeric input: {num1}, {num2}")
        print(f"Invalid numbers: {num1}, {num2}")
    except Exception as error:
        logging.error(f"Unexpected error: {error}")
        print(f"An error occurred: {error}")

@execution_logger
def start_repl(command_registry):
    print("Calculator REPL started. Type 'exit' to leave.")
    print("Append 'mp' to use multiprocessing.")

    while True:
        user_input = input(">> ")
        if user_input.lower() == 'exit':
            print("Closing REPL.")
            break
        elif user_input.lower() == 'menu':
            print("Available operations:")
            for cmd in command_registry:
                print(f"- {cmd}")
            continue
        elif user_input.lower() == 'history':
            history = Calculations.get_all_calculations()
            print("No history available." if history.empty else history)
            continue
        elif user_input.lower() == 'clear_history':
            Calculations.clear_history()
            print("History cleared.")
            continue
        elif user_input.startswith('save_history'):
            _, path = user_input.split(maxsplit=1)
            Calculations.save_history(path)
            print(f"History saved to {path}")
            continue
        elif user_input.startswith('load_history'):
            _, path = user_input.split(maxsplit=1)
            if os.path.exists(path):
                Calculations.load_history(path)
                print(f"History loaded from {path}")
            else:
                print(f"File not found: {path}")
            continue
        elif user_input.startswith('delete_history'):
            _, idx = user_input.split(maxsplit=1)
            try:
                Calculations.delete_history(int(idx))
            except Exception as e:
                print(f"Error deleting entry: {e}")
            continue
        elif user_input.startswith('filter_with_operation'):
            _, op_name = user_input.split(maxsplit=1)
            filtered = Calculations.filter_with_operation(op_name)
            print(f"No entries found for operation '{op_name}'." if filtered.empty else filtered)
            continue

        parts = user_input.split()
        if len(parts) not in [3, 4]:
            print("Format: <operation> <num1> <num2> [mp]")
            continue

        op, val1, val2 = parts[:3]
        use_mp = len(parts) == 4 and parts[3].lower() == 'mp'

        if op not in command_registry:
            print(f"Operation '{op}' not recognized.")
            continue

        execute_operation(val1, val2, op, command_registry, use_mp)

@execution_logger
def main():
    commands = discover_plugins()

    if len(sys.argv) == 4:
        _, val1, val2, op = sys.argv
        execute_operation(val1, val2, op, commands)
    elif len(sys.argv) == 5:
        _, val1, val2, op, flag = sys.argv
        execute_operation(val1, val2, op, commands, flag.lower() == 'mp')
    elif len(sys.argv) == 2 and sys.argv[1].lower() == 'repl':
        start_repl(commands)
    else:
        print("Usage: python run_app.py <num1> <num2> <operation> [mp] | python run_app.py repl")

if __name__ == '__main__':
    env = initialize_environment()
    configure_logging(log_level=env.get("LOG_LEVEL", "INFO").upper())
    logging.info(f"Environment mode: {env.get('ENVIRONMENT', 'Development')}")
    logging.info("Calculator Application Launched.")
    main()

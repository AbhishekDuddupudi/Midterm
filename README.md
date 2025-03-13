
# 🧮 Advanced Python Calculator — Midterm Project

```
(.venv) @AbhishekDuddupudi ➜ /workspaces/Midterm (main) $ python3 main.py repl
2025-03-13 16:56:25,021 - root - INFO - Environment mode: Development
2025-03-13 16:56:25,022 - root - INFO - Calculator Application Launched.
2025-03-13 16:56:25,022 - root - INFO - Running main
2025-03-13 16:56:25,022 - root - INFO - Plugin loaded: subtract_command
2025-03-13 16:56:25,023 - root - INFO - Plugin loaded: divide_command
2025-03-13 16:56:25,023 - root - INFO - Plugin loaded: add_command
2025-03-13 16:56:25,023 - root - INFO - Plugin loaded: mean_command
2025-03-13 16:56:25,024 - root - INFO - Plugin loaded: mode_command
2025-03-13 16:56:25,024 - root - INFO - Plugin loaded: median_command
2025-03-13 16:56:25,024 - root - INFO - Plugin loaded: multiply_command
2025-03-13 16:56:25,024 - root - INFO - Running start_repl
Calculator REPL started. Type 'exit' to leave.
Append 'mp' to use multiprocessing.
>> add 12 2 
2025-03-13 16:56:36,000 - root - INFO - Running execute_operation
2025-03-13 16:56:36,000 - root - INFO - Result: 14
12 add 2 = 14
>> save_history data/calculations.csv
History saved to data/calculations.csv
>> clear_history
History cleared.
```

## 📌 Project Snapshot
This project delivers an **interactive calculator application**, developed in Python, that runs in the terminal and provides **real-time calculations**. It's designed with a modular architecture, leveraging **design patterns**, **logging**, **plugin extensibility**, and **data persistence** using Pandas.  

The calculator can handle both **basic arithmetic** and **statistical operations**, offering flexibility for future enhancements.

## 🔧 Key Capabilities

### ✅ Interactive REPL  
A Read-Eval-Print Loop (REPL) allows users to enter commands, get immediate feedback, and perform operations like addition, subtraction, and more advanced statistical functions.

### ✅ Extensible Plugin System  
New operations can be added simply by dropping new plugin files into the designated folder. No changes to the core app are required.

### ✅ Calculation History  
Every calculation can be logged into a Pandas DataFrame and saved to CSV for reference. You can load previous histories or clear them at any time.

### ✅ Logging for Transparency  
The system uses Python's `logging` library to track events:
- Tracks plugin loading
- Logs each command execution
- Records when history is saved/cleared
- Supports configurable log levels

### ✅ Design Patterns Implemented
- **Command Pattern**: Each calculation type is encapsulated as its own command class.
- **Facade Pattern**: Simplifies access to history management.
- **Factory Method**: Dynamically loads plugins without modifying core code.
- **Singleton Pattern**: Ensures one instance for core services like history manager.
- **Strategy Pattern**: Allows swapping calculation logic seamlessly.

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Git (to clone the repository)

## 🛠️ Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd <repository-folder>
```

### 2. Set Up the Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root:
```
ENVIRONMENT=Development
LOG_LEVEL=INFO
LOG_FILE=logs/app.log
```

## ▶️ Running the Calculator

### Start REPL Mode
```bash
python3 main.py repl
```

### Available Commands Inside REPL:
- `add 10 5`  
- `subtract 9 3`  
- `multiply 2 4`  
- `divide 8 2`  
- `mean 4 10`  
- `median 5 15`  
- `mode 6 6`  

### History Management Commands:
- `history` — View past calculations  
- `save_history data/filename.csv` — Save history to CSV  
- `load_history data/filename.csv` — Load previous history  
- `delete_history <index>` — Delete a specific history record  
- `clear_history` — Clear all history  

## ✅ Logging & Configuration

The system uses structured logs for better visibility.  
Configure the logging level and file through environment variables in `.env`:
```
LOG_LEVEL=DEBUG
LOG_FILE=logs/app.log
```

Example logs:
```
2025-03-13 16:56:25,022 - root - INFO - Calculator Application Launched.
2025-03-13 16:56:36,000 - root - INFO - Result: 14
```

## 🧰 Error Handling Practices

### LBYL (Look Before You Leap)
- Checks if history files exist before loading.

### EAFP (Easier to Ask for Forgiveness than Permission)
- Handles invalid operations with `try-except` blocks.
  
```python
try:
    result = command.execute(num1, num2)
except ZeroDivisionError:
    logging.error("Cannot divide by zero.")
```

## 📂 Project Structure
```
project_root/
├── app/
│   ├── core/               # Core logic (commands, calculations, facade)
│   └── plugins/            # Plugin commands (add, subtract, mean, etc.)
├── data/                   # Saved calculation histories
├── logs/                   # Application logs
├── tests/                  # Unit tests for commands and plugins
├── main.py                 # Entry point for REPL
├── requirements.txt
└── README.md
```

## 🧪 Running Tests
Run unit tests with coverage reporting:
```bash
pytest --cov=app --cov-report=term-missing
```

## ✅ Design Principles
- **Extensibility**: Add new calculation logic without changing the core.
- **Loose Coupling**: Commands and REPL logic are decoupled.
- **Scalability**: Modular structure supports future expansion.

## 💻 Commit Best Practices
Each feature or fix is committed with descriptive messages:
```
"Refactored REPL to support multiprocessing operations"
"Added MeanCommand with multiprocessing support"
"Improved history management with PandasFacade"
```

## 🎥 Demo Video
👉 

## 🌐 Environment Variables Reference
| Variable     | Description                 | Example           |
|--------------|-----------------------------|-------------------|
| ENVIRONMENT  | App mode (Development/Prod) | Development       |
| LOG_LEVEL    | Logging level               | DEBUG / INFO      |
| LOG_FILE     | Log file output path        | logs/app.log      |

## ✅ Author
- **Abhishek Duddupudi**

## ✅ Conclusion
This advanced calculator application demonstrates:
- Clean code  
- Scalable architecture  
- Dynamic plugin handling  
- Clear and robust logging  
- Well-tested functionality  


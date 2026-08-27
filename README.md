# Log Analyzer

A lightweight, command-line log file analysis tool built with Python. 
This project is designed as a practical learning sandbox to master **Git workflows**, **pytest** testing, and the **logging** module in a real-world context.

Instead of a generic to-do list or calculator, this tool reads system/application log files, parses them, generates statistical reports, and extracts critical errors—making it both useful and educational.

## Features

- **Log Parsing**: Reads standard log lines formatted as `[timestamp] LEVEL: message`.
- **Statistics**: Counts log entries by level (INFO, WARNING, ERROR, etc.).
- **Error Extraction**: Displays the first 10 error messages for quick debugging.
- **Command-Line Interface**: Accepts the log file path as an argument.
- **Integrated Logging**: Logs its own operations (info, warnings, errors) to both the console and a dedicated `logs/app.log` file.
- **Tested with pytest**: Includes unit tests with coverage reports.

## Project Structure

```text
log_analyzer/
├── .gitignore                # Ignores logs/ and Python cache
├── README.md                 # This file
├── requirements.txt          # Dependencies (e.g., pytest, pytest-cov)
├── log_analyzer/             # Main package
│   ├── __init__.py
│   ├── cli.py                # Entry point, argument parsing (argparse)
│   ├── parser.py             # Core logic: parse a single log line
│   ├── reporter.py           # Statistics generation from parsed lines
│   └── logger_config.py      # Logging setup (file + console handlers)
├── tests/                    # Unit tests
│   ├── test_parser.py        # Tests for parsing logic
│   └── test_reporter.py      # Tests for report generation
└── sample.log                # Example log file for quick testing

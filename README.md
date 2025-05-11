# DollarDiet CLI (with JSON Saving)

DollarDiet is a CLI-based budget tracker designed for the $1 Challenge. It lets you add daily expenses, classifies them as essential or luxury, and stores your data in a JSON file.

## Features

- Add new expenses with name, amount, and category
- Classifies each expense as **Essential** or **Luxury**
- Calculates total spent and remaining amount
- Warns if $1 budget is exceeded
- Saves all expenses in `expenses.json` file
- Loads data automatically every time the app runs

## OOP Concepts Used

- Classes (`Expense`, `DollarDiet`)
- Methods, object composition
- File handling using JSON
- Static methods and data persistence

## How to Run

1. Make sure you have Python 3 installed
2. Save both `dollardiet.py` and `expenses.json` in the same folder (JSON will be created automatically)
3. Open terminal in that folder and run:
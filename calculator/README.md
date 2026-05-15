PySide6 Calculator Application

An object-oriented-programming based GUI calculator built
with Python and PySide6.
Uses a modular structure with separated UI and calculation logic.

Features:
Basic arithmetic operations (+, -, *, /, %, √).
Decimal input support.
Clear (C) and backspace (X).
Qt Designer UI integration (.ui files).
Event-driven button handling.
String-based expression evaluation.

Project Structure:
calculator/
__init__.py
buttons.py
calculator.py
README.md

gui/
__init__.py
mainwindow.py
ui_mainwindow.py
ui_calculator.ui

src/
__init__.py
calc.py

Usage:
Run the application - python calculator.py.

Architecture:
gui/ — UI layer (PySide6 windows, signals, events),
src/ — calculation logic (Calculator class),
calculator.py — application entry point.

Logic:
Expression is built as a string.
Calculator evaluates full expression.
UI sends button input, displays result.

Requirements:
PySide6.
Python 3.10+.

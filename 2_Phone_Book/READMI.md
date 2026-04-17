PhoneBook CLI Application

A function-based command-line phone book application for managing contacts,
with support for JSON storage.

Features
Add, view, search, edit, and delete contacts
Persistent storage using JSON files
Simple command-line interface

Project Structure
main_pb.py            # Entry point
helper_pb.py          # Core logic and helper functions

phone_book.json       # Main storage file
phone_book_tests.json # Test storage file

Usage

Run the application:

python main_pb.py

Menu
1 — Show all contacts
2 — Search contacts
3 — Edit first name
4 — Edit last name
5 — Edit phone numbers
6 — Delete contact
7 — Add contact
8 — Create a new phone book
Q — Quit the application
ANY — Continue

Storage
Data is stored in a JSON file
Changes are saved automatically after each modification
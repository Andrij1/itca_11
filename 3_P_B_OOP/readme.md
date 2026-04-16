PhoneBook CLI Application

A simple command-line phone book application for managing contacts with
support for multiple storage formats (JSON, CSV, SQLite).

Features
Add, view, search, edit, and delete contacts
Store multiple phone numbers (mobile, work, home)
Save data in JSON, CSV, and SQLite simultaneously
Project Structure
main.py            # Entry point
contact.py         # Contact model
book.py            # PhoneBook logic
finder.py          # Search functionality
cli.py             # CLI helpers

converters.py      # Data converters
storages_3.py      # Storage implementations

data_3/            # Storage files
Usage

Run the application:

python main.py
Menu
1 — Show all contacts
2 — Search
3 — Edit name
4 — Edit phone numbers
5 — Edit email
6 — Edit address
7 — Delete contact
8 — Add contact
9 — New phone book
QS — Save and quit
0 — Quit without saving
Storage

Data is loaded and saved using a multi-storage system:

JSON
CSV
SQLite

Changes are saved only when exiting with QS.



PhoneBook CLI Application

An OOP-based command-line phone book application for managing contacts, 
with support for multiple storage formats (JSON, CSV, SQLite).

Features

Add, view, search, edit, and delete contacts
Store multiple phone numbers (mobile, work, home)
Edit email and address fields
Save data in JSON, CSV, and SQLite simultaneously

Project Structure

main.py            # Entry point
app_setup.py       # Application setup (loads PhoneBook + storages)

choice.py          # Main menu loop (controller / command router)
choice_handler.py  # CLI menu + user input handling
cli.py             # Contact creation (CLI input logic)

contact.py         # Contact model
book.py            # PhoneBook logic (in-memory storage + operations)
converters.py      # Data converters (JSON / CSV / DB formats)
storages.py        # Storage implementations (MultiStorage, JSON, CSV, SQLite)

data/              # Storage of book files
tests/             # Storage of pytest files

Usage

Run the application:

python main.py

Menu:

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

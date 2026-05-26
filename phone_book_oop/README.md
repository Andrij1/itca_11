# PhoneBook CLI Application

An object-oriented command-line phone book application for managing contacts,
with support for multiple storage formats (JSON, CSV, SQLite).

---

## Features

- Add, view, search, edit, and delete contacts
- Store multiple phone numbers (mobile, work, home)
- Edit email and address fields
- Persistent storage in JSON, CSV, and SQLite formats
- Modular OOP architecture with clear separation of concerns

---

## Project Structure

```text
PhoneBook Project
│
├── main.py                 # Entry point
├── app_setup.py            # Initializes PhoneBook + storage system
│
├── choice.py              # Main menu loop (controller / router)
├── choice_handler.py      # CLI input handling and menu actions
├── cli.py                 # Contact creation (user input logic)
│
├── contact.py            # Contact model (data structure)
├── book.py               # PhoneBook logic (in-memory operations)
├── converters.py         # Data converters (JSON / CSV / SQLite)
├── storages.py           # Multi-storage system implementation
│
├── data/                 # Stored phone book files
└── tests/                # Pytest test suite
```

---

## Usage

Run the application:

```bash
python main.py
```

---

## Menu Options

```text
1 — Show all contacts
2 — Search contacts
3 — Edit name
4 — Edit phone numbers
5 — Edit email
6 — Edit address
7 — Delete contact
8 — Add contact
9 — Create new phone book
QS — Save and quit
0 — Quit without saving
```

---

## Storage System

The application uses a multi-storage architecture:

- JSON storage
- CSV storage
- SQLite database

### Behavior
- Data is loaded on startup
- Data is saved only when exiting with `QS`
- Ensures consistent synchronization across all formats
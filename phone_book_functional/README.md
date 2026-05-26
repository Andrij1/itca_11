# PhoneBook CLI Application

A command-line phone book application built with Python using a function-based
architecture. It allows users to manage contacts with persistent JSON storage.

---

## Features

- Add, view, search, edit, and delete contacts
- Persistent storage using JSON files
- Simple and interactive command-line interface
- Automatic saving after every modification

---

## Project Structure

```text
main.py            # Entry point
helper.py          # Core logic and helper functions

book.json          # Main storage file
book_tests.json    # Test storage file
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
3 — Edit first name
4 — Edit last name
5 — Edit phone numbers
6 — Delete contact
7 — Add contact
8 — Create a new phone book
Q — Quit the application
ANY — Return to menu / continue
```

---

## Storage

- Contacts are stored in JSON format
- All changes are saved automatically after each operation
- Data persists between program runs
```
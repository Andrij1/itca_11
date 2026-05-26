import json
import csv
import sqlite3
from converters import JsonConverter, CSVConverter, DBConverter


class MultiStorage:

    def __init__(self, storages):
        self.storages = storages


    def uniques(self, contacts):
        return sorted(
            set(contacts),
            key=lambda c: (c.firstname.lower(), c.lastname.lower())
        )


    def write(self, contacts):
        sorted_contacts = self.uniques(contacts)
        for storage in self.storages:
            storage.write(sorted_contacts)
        return sorted_contacts


    def load(self):
        all_contacts = []
        for storage in self.storages:
            all_contacts.extend(storage.load())
        return self.uniques(all_contacts)


class JsonStorage:

    def __init__(self, filename):
        self.filename = filename

    def write(self, contacts):
        data = [JsonConverter.to_dict(c) for c in contacts]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)


    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
                return [JsonConverter.from_dict(d) for d in data]
        except FileNotFoundError:
            return []


class CSVStorage:

    def __init__(self, filename):
        self.filename = filename


    def write(self, contacts):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["firstname", "lastname", "numbers", "email", "address"])
            for c in contacts:
                writer.writerow(CSVConverter.to_row(c))


    def load(self):
        try:
            with open(self.filename, "r") as f:
                reader = csv.reader(f)
                next(reader)
                return [CSVConverter.from_row(r) for r in reader]
        except FileNotFoundError:
            return []


class DBStorage:

    def __init__(self, filename):
        self.filename = filename


    def create_table(self):
        self.connection = sqlite3.connect(self.filename)
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Phonebook (
                    Firstname TEXT,
                    Lastname TEXT,
                    Numbers TEXT,
                    Email TEXT,
                    Address TEXT
                )
            """)
            conn.commit()


    def write(self, contacts):
        self.create_table()
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Phonebook")

            data = [DBConverter.to_list(c) for c in contacts]

            cursor.executemany("""
                INSERT INTO Phonebook VALUES (?, ?, ?, ?, ?)
            """, data)

            conn.commit()


    def load(self):
        self.create_table()
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT * FROM Phonebook
                ORDER BY Firstname COLLATE NOCASE,
                         Lastname COLLATE NOCASE
            """)
            rows = cursor.fetchall()

        return [DBConverter.from_list(r) for r in rows]

import json
import csv
import sqlite3
from converters import JsonConverter, CSVConverter, DBConverter


class MultiStorage:

    def __init__(self, storages):
        self.storages = storages
        
    
    def uniques(self, contacts):
        seen = set()
        unique_contacts = []
        contacts_sorted = sorted(contacts, key = lambda con: (con.firstname.lower(), con.lastname.lower()))
        for contact in contacts_sorted:
            key = (
                contact.firstname,
                contact.lastname,
                tuple(sorted((lbl, num) for lbl, num in contact.numbers)),
                contact.email,
                contact.address
                )
            if key not in seen:
                seen.add(key)
                unique_contacts.append(contact)
                    
        return unique_contacts
    

    def contacts_sorted(self, contacts):
        unique_contacts = self.uniques(contacts)
        sorted_contacts = sorted(unique_contacts,
                key = lambda c: (c.firstname.lower(), c.lastname.lower()))
        
        return sorted_contacts

     
    def write(self, contacts):
        sorted_contacts = self.contacts_sorted(contacts)
        for storage in self.storages:
            storage.write(sorted_contacts)
            
        return sorted_contacts


    def load(self):
        all_contacts = []
        for storage in self.storages:
             all_contacts.extend(storage.load())

        return self.contacts_sorted(all_contacts)

    
class JsonStorage:

    def __init__(self, filename):
        self.filename = filename
        

    def write(self, sorted_contacts):
        data = [JsonConverter.to_dict(contact) for contact in sorted_contacts]
        with open(self.filename, 'w') as json_file:
            json.dump(data, json_file, indent = 4)
            

    def load(self):
        try:
            with open(self.filename, "r") as json_book_file:
                data = json.load(json_book_file)
                return [JsonConverter.from_dict(d) for d in data]
            
        except FileNotFoundError:
            return []

                  
class CSVStorage:

    def __init__(self, filename):
        self.filename = filename

    def write(self, sorted_contacts):              
        with open(self.filename, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(
                    ["firstname", "lastname", "numbers", "email", "address"]
                    )
            for c in sorted_contacts:
                writer.writerow(CSVConverter.to_row(c))

    def load(self):
        try:
            with open(self.filename, 'r') as csv_book_file:
                reader = csv.reader(csv_book_file)
                next(reader)
                return [CSVConverter.from_row(row) for row in reader]

        except FileNotFoundError:
            return []


class DBStorage:

    def __init__(self, filename):
        self.filename = filename

    def create_table(self):
        self.connection = sqlite3.connect(self.filename)
        with self.connection as self.conn:
            self.cursor = self.conn.cursor()
            self.db_create = ('''
                CREATE TABLE IF NOT EXISTS Phonebook (
                Firstname TEXT NOT NULL, Lastname TEXT NOT NULL,
                Numbers TEXT, Email TEXT, Address TEXT)
            ''')
            self.cursor.execute(self.db_create)
            self.conn.commit()

    def write(self, sorted_contacts):
        self.create_table()
        with self.connection as self.conn:
            self.cursor.execute('DELETE FROM Phonebook')
            self.conn.commit()

            data = [DBConverter.to_list(c) for c in sorted_contacts]

            self.cursor.executemany('''
                INSERT INTO Phonebook (Firstname, Lastname, Numbers, Email, Address)
                Values (?, ?, ?, ?, ?) ''',
                data
                )        

            self.conn.commit()        
            
        print("--> THE Writing DEBUG TRICK <--")    # data[0] - 1st row
        if data:
            print(data[0], len(data[0]))        # len(data[0]) - all cols of the row
       
    
    def load(self):
        self.create_table()
        with self.connection as self.conn:
            self.cursor.execute('''
                SELECT * FROM Phonebook
                ORDER BY
                Firstname COLLATE NOCASE,
                Lastname COLLATE NOCASE
            ''')        
            lines = self.cursor.fetchall()
                    
        print("--> THE Loading DEBUG TRICK <--")
        if lines:
            print(lines[0], len(lines[0]))

        return [DBConverter.from_list(line) for line in lines]



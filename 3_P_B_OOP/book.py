
from contact import Contact
from storages_3 import MultiStorage, JsonStorage, CSVStorage, DBStorage
from converters import JsonConverter, CSVConverter, DBConverter

class PhoneBook:

    def __init__(self):
        self.book = []
        self.to_write = False


    def add_contact(self, contact):
        self.book.append(contact)
        self.to_write = True
        
    
    def remove_contact(self, contact):
        if contact in self.book:
            self.book.remove(contact)
            self.to_write = True
            

    def find_contact(self, firstname, lastname):
        return [
            c for c in self.book
            if c.firstname.lower() == firstname.lower()
            and c.lastname.lower() == lastname.lower()
        ]


    def list_contacts(self):
        return self.book.copy()


    def __contains__(self, contact):
        return contact in self.book


    def __len__(self):
        return len(self.book)


    def __iter__(self):
        return iter(self.book)


    def __getitem__(self, index):
        return self.book[index]


    def __eq__(self, other):
        if not isinstance(other, Contact):
            return NotImplementedError
        return (
            self.firstname == other.firstname and
            self.lastname == other.lastname
            )


    def __str__(self):
        return '\n' + '\n'.join(str(c) for c in self.book)

    


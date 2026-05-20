from contact import Contact
from storages import MultiStorage, JsonStorage, CSVStorage, DBStorage
from converters import JsonConverter, CSVConverter, DBConverter

class PhoneBook:
    """In-memory contact book for Contact objects storing and manipulating."""

    def __init__(self):
        self.book = []
        self.to_write = False


    def add_contact(self, contact):
        """Adds the new spicific Contact to the phone book."""
        self.book.append(contact)
        self.to_write = True
        
    
    def remove_contact(self, contact):
        """Removes the specific Contact from the phone book, if it exists."""
        if contact in self.book:
            self.book.remove(contact)
            self.to_write = True


    def find_contact(self):
        """Finds the specific Contact by name, if exists."""
        firstname = input('Enter firstname :\n-> ').strip()
        lastname = input('Enter lastname :\n-> ').strip()
        found = []
        for contact in self.book:
            if (
                contact.firstname.lower() == firstname.lower()
                and
                contact.lastname.lower() == lastname.lower()

            ):
                found.append(contact)

        if found:
            try:
                for i, c in enumerate(found):
                    print(f'index - {i} : {c}')
                idx = int(input('Enter needed contact index :\n -> '))
                con = found[idx]

                return con, firstname, lastname
            except ValueError as e:
                print(e)
                return None, firstname, lastname
        else:
            print('\n-> Contact not found')
            return None, firstname, lastname


    def list_contacts(self):
        """Shows all Contacts copy form the phone book."""
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
            return NotImplemented
        return (
            self.firstname == other.firstname and
            self.lastname == other.lastname
            )


    def __str__(self):
        return '\n' + '\n'.join(str(c) for c in self.book)

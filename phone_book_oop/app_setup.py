from contact import Contact
from book import PhoneBook
from converters import JsonConverter, CSVConverter, DBConverter
from storages import MultiStorage, JsonStorage, CSVStorage, DBStorage


def setup_app():
    phonebook = PhoneBook()
    json_storage = JsonStorage("data/book.json")
    csv_storage = CSVStorage("data/book.csv")
    db_storage = DBStorage("data/book.sqlite")
    storages = MultiStorage([json_storage, csv_storage, db_storage])

    try:
        phonebook.book = storages.load().copy()
        for c in phonebook.book:
            to_write = False
        print(phonebook)
    except FileNotFoundError as e:
        print(e)

    return phonebook, storages

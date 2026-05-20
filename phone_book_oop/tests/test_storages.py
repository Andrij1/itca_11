import sys
sys.path.append('../')

import pytest
from contact import Contact
from book import PhoneBook
from storages import MultiStorage, JsonStorage, CSVStorage, DBStorage


def set_all_contacts():
    c = Contact("Kevin", "Smith", mobile="345", email="a")
    c1 = Contact("Kevin", "Smith", mobile="345", email="a")
    c2 = Contact("HELEN", "KRUGER", mobile="+3405", email="b")

    return (c, c1, c2)


@pytest.fixture()
def contacts():
    return set_all_contacts()


@pytest.fixture()
def phonebook(contacts):
    pb = PhoneBook()
    for c in contacts:
        pb.add_contact(c)
    return pb


@pytest.fixture()
def storages():
    js = JsonStorage('data/phonebook.json')
    csv = CSVStorage('data/phonebook.csv')
    db = DBStorage('data/phonebook.sqlite')
    return [js, csv, db]


@pytest.fixture()
def multistorage(storages):
    return MultiStorage(storages)


def test_unique_contacts(multistorage, contacts):
    result = multistorage.uniques(contacts)

    assert len(result) == 2


def test_sorted_contacts(multistorage, contacts):
    result = multistorage.contacts_sorted(contacts)

    assert result[0].firstname in ["HELEN", "Kevin"]


def test_compare_equal_contacts(phonebook):
    assert phonebook[0] == phonebook[1]


def test_compare_different_contacts(phonebook):
    assert phonebook[0] != phonebook[2]


def test_storages_write(multistorage, contacts):
    lst = multistorage.write(contacts)

    assert len(lst) == 2


def test_storages_load(multistorage):
    lst = multistorage.load()

    assert isinstance(lst, list)
    assert len(lst) >= 0

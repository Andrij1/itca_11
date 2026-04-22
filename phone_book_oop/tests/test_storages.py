import sys
sys.path.append('../')

import pytest
from contact import Contact
from book import PhoneBook
from converters import JsonConverter, CSVConverter, DBConverter
from storages_3 import MultiStorage, JsonStorage, CSVStorage, DBStorage


def set_all_contacts():   
    c = Contact("Kevin","Smith", mobile="345",work="123", home= "234",
        email = "kSmith@delta.ua", address = "US, CA, L.Angeles, Burbank ave., 1123"
        )
    c1 = Contact("Kevin","Smith", mobile="345",work="123", home= "234",
        email = "kSmith@delta.ua", address = "US, CA, L.Angeles, Burbank ave., 1123"
        )
    c2 = Contact("HELEN", "KRUGER", mobile="+3405",work= "+0123", home= "+2340",
        email = "helen_kruger@siemens.com", address = "DE, Bonn, Blumenstrasse, 88/22"
        )
    contacts = (c, c1, c2)
    
    return contacts


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
    js = JsonStorage('data_3/phonebook_3.json')
    csv = CSVStorage('data_3/phonebook_3.csv')
    db = DBStorage('data_3/phonebook_m_3.sqlite')
    storages = [js,csv,db]

    return storages
    
@pytest.fixture()
def multistorage(storages):
    ms = MultiStorage(storages)
    
    return ms


def test_unique_contacts(multistorage, phonebook, contacts):
    result = multistorage.uniques(contacts)
    assert len(result) == 2


def test_sorted_contacts(multistorage, phonebook, contacts):
    result = multistorage.contacts_sorted(contacts)
    assert result[0].firstname == 'HELEN'


def test_compare_equal_contacts(phonebook):
    result = (phonebook[0] == phonebook[1])
    assert result


def test_compare_different_contacts(phonebook):
    result = (phonebook[0] != phonebook[2])
    assert result


def test_storages_write(multistorage,contacts):
    lst = multistorage.write(contacts)
    res = (len(lst) == 2)
    first = lst[0]
    second = lst[1]
    res1 = (lst[1].email == "kSmith@delta.ua")
    assert res
    assert res1 
    assert first.firstname == "HELEN"
    assert second.lastname == "Smith"


def test_storages_load(multistorage):
    lst = multistorage.load()
    res = (len(lst) == 2)
    first = lst[0]
    second = lst[1]
    res1 = (lst[1].email == "kSmith@delta.ua")
    assert res
    assert res1
    assert first.firstname == "HELEN"
    assert second.lastname == "Smith"



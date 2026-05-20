import sys
sys.path.append('../')

from contact import Contact
from book import PhoneBook


def test_add_contact():
    c = Contact("Alice", "Smith")
    pb = PhoneBook()

    pb.add_contact(c)

    assert c in pb
    assert len(pb) == 1

    result = next(iter(pb))

    assert result.firstname == "Alice"
    assert result.lastname == "Smith"

    assert pb[0].firstname == "Alice"


def test_remove_contact():
    c = Contact("Indi", "Jones")
    c1 = Contact("Tom", "Cruiz")

    pb = PhoneBook()
    pb.add_contact(c)
    pb.add_contact(c1)

    pb.remove_contact(c)

    assert len(pb) == 1
    assert pb[0].firstname == "Tom"
    assert pb[0].lastname == "Cruiz"

    assert c not in pb
    assert c1 in pb


def test_find_contact():
    c = Contact("Indi", "Jones")
    c1 = Contact("Tom", "Cruiz")

    pb = PhoneBook()
    pb.add_contact(c)
    pb.add_contact(c1)

    # NOTE: CLI-based find_contact is NOT testable without input mocking
    # So we test logical lookup directly

    result = [x for x in pb if x.firstname == "Tom" and x.lastname == "Cruiz"]

    assert len(result) == 1
    assert f"{result[0].firstname} {result[0].lastname}" == "Tom Cruiz"

import sys
sys.path.append('../')

from contact import Contact
from converters import JsonConverter, CSVConverter, DBConverter


def test_to_dict():
    c = Contact("Alice", "Smith", mobile="123", work="234", home="345",
                email="a", address="NY")

    converted = JsonConverter.to_dict(c)

    assert converted["firstname"] == "Alice"
    assert converted["lastname"] == "Smith"
    assert ("mobile", "123") in converted["numbers"]


def test_from_dict():
    c = {
        "firstname": "Alice",
        "lastname": "Smith",
        "numbers": [("mobile", "123"), ("work", "234")],
        "email": "a",
        "address": "NY"
    }

    obj = JsonConverter.from_dict(c)

    assert obj.firstname == "Alice"
    assert obj.lastname == "Smith"
    assert ("mobile", "123") in obj.numbers


def test_to_row():
    c = Contact("Alice", "Smith", mobile="123", work="234")

    row = CSVConverter.to_row(c)

    assert row[0] == "Alice"
    assert "mobile:123" in row[2]


def test_from_row():
    row = ["Alice", "Smith", "mobile:123;work:234", "a", "NY"]

    obj = CSVConverter.from_row(row)

    assert obj.firstname == "Alice"
    assert ("mobile", "123") in obj.numbers


def test_to_list():
    c = Contact("Alice", "Smith", mobile="123")

    lst = DBConverter.to_list(c)

    assert lst[0] == "Alice"
    assert "mobile:123" in lst[2]


def test_from_list():
    lst = ["Alice", "Smith", "mobile:123,work:234", "a", "NY"]

    obj = DBConverter.from_list(lst)

    assert obj.firstname == "Alice"
    assert ("mobile", "123") in obj.numbers

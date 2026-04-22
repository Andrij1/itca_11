import sys
sys.path.append('../')

from contact import Contact
from book import PhoneBook
from converters import JsonConverter, CSVConverter, DBConverter


def test_to_dict():
    
    pb = PhoneBook()
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )    
    pb.add_contact(c)
    
    converted = JsonConverter.to_dict(c)
    expected = {
            "firstname": "Alice",
            "lastname": "Smith",
            "numbers":
            [
                ("mobile", "123"),
                ("work", "234"),
                ("home", "345")
            ],
            "email": "Alice@ua",
            "address": "US, NY, Washington ave., 1126"
        }
    
    result_n = (converted == expected)
    assert result_n


def test_from_dict():
    
    pb = PhoneBook()
    c = {
            "firstname": "Alice",
            "lastname": "Smith",
            "numbers":
            [
                ("mobile", "123"),
                ("work", "234"),
                ("home", "345")
            ],
            "email": "Alice@ua",
            "address": "US, NY, Washington ave., 1126"
        }
    
    converted_fr_d = JsonConverter.from_dict(c)
    
    assert converted_fr_d.firstname == "Alice"
    assert converted_fr_d.lastname == "Smith"
    assert converted_fr_d.numbers == [
                ("mobile", "123"),
                ("work", "234"),
                ("home", "345")
            ]
    assert converted_fr_d.email == 'Alice@ua'
    assert converted_fr_d.address == "US, NY, Washington ave., 1126"


def test_to_row():
    pb = PhoneBook()
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )    
    pb.add_contact(c)
    
    converted = CSVConverter.to_row(c)
    expected = [
        'Alice', 'Smith', 'mobile:123;work:234;home:345',
        'Alice@ua', 'US, NY, Washington ave., 1126'
    ]
    result = (converted == expected)
    
    assert result


def test_from_row():

    pb = PhoneBook()
    c = [
        'Alice', 'Smith', 'mobile:123;work:234;home:345',
        'Alice@ua', 'US, NY, Washington ave., 1126'
    ]
    pb.add_contact(c)
    
    converted_fr_r = CSVConverter.from_row(c)
    
    assert converted_fr_r.firstname == "Alice"
    assert converted_fr_r.lastname == "Smith"
    assert converted_fr_r.numbers == [
                ("mobile", "123"),
                ("work", "234"),
                ("home", "345")
            ]
    assert converted_fr_r.email == 'Alice@ua'
    assert converted_fr_r.address == "US, NY, Washington ave., 1126"


def test_to_list():

    pb = PhoneBook()
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )    
    pb.add_contact(c)
    converted_to_l = DBConverter.to_list(c)
    expected = [
        'Alice', 'Smith', 'mobile:123,work:234,home:345',
        'Alice@ua', 'US, NY, Washington ave., 1126'
        ]
    result = (converted_to_l == expected)
    
    assert result


def test_from_list():
    
    pb = PhoneBook()
    c = [
        'Alice', 'Smith', 'mobile:123,work:234,home:345',
        'Alice@ua', 'US, NY, Washington ave., 1126'
        ]
    pb.add_contact(c)
    
    converted_fr_l = DBConverter.from_list(c)
    
    assert converted_fr_l.firstname == "Alice"
    assert converted_fr_l.lastname == "Smith"
    assert converted_fr_l.numbers == [
                ("mobile", "123"),
                ("work", "234"),
                ("home", "345")
            ]
    assert converted_fr_l.email == 'Alice@ua'
    assert converted_fr_l.address == "US, NY, Washington ave., 1126"

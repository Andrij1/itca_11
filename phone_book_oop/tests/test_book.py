import sys
sys.path.append('../')

from contact import Contact
from book import PhoneBook


def test_add_contact():
    c = Contact(
        "Alice", "Smith"
        )
    pb = PhoneBook()

    pb.add_contact(c)

    assert c in pb
    assert len(pb) == 1
    
    result = None
    for i in pb:
         result = i
         print(result)
    res = (result.firstname == "Alice")
    res1 = (result.lastname == "Smith")
    assert res and res1
    
    result1 = (pb[0].firstname == 'Alice')
    assert result1
    

def test_remove_contact():
    c = Contact(
        'Indi', 'Jones'
        )
    c1 = Contact(
        'Tom', 'Cruiz'
        )
    pb = PhoneBook()
    pb.add_contact(c)
    pb.add_contact(c1)
    pb.remove_contact(c)
    assert len(pb) == 1
    assert pb[0].firstname == 'Tom'
    assert pb[0].lastname == 'Cruiz'        
    assert c not in pb    
    assert c1 in pb


def test_find_contact():
    c = Contact(
        'Indi', 'Jones'
        )
    c1 = Contact(
        'Tom', 'Cruiz'
        )
    pb = PhoneBook()
    pb.add_contact(c)
    pb.add_contact(c1)

    result = pb.find_contact('Tom', 'Cruiz')
    
    assert f'{result[0].firstname} {result[0].lastname}' == 'Tom Cruiz'        
    assert len(result) == 1



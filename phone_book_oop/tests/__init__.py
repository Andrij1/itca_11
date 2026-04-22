import sys
sys.path.append('../')
from contact import Contact
import contact
print("CONTACT FILE:", contact.__file__)
print(Contact is contact.Contact)

def test_contact_name_create():
    c = Contact(
        "Alice", "Smith"
        )

    assert c.firstname == 'Alice'
    assert c.lastname == 'Smith'

    #print(c)


#test_contact_name_create()


def test_numbers_create():
    c = Contact(
        firstname = None, lastname = None,
        mobile="123", work="234", home="345"
        )

    assert ('mobile','123') in c.numbers
    assert ('work', '234') in c.numbers
    assert ('home', '345') in c.numbers

    #print(c)



def test_amend_contact_name():
    c = Contact(
        "Alice", "Smith"
        )
    c.amend_contact_name(new_firstname = "SEAN")
    c.amend_contact_name(new_lastname = "CONNARY")

    assert c.firstname == "SEAN"
    assert c.lastname == "CONNARY"

    #print(c)
    
#test_amend_contact_name()


def test_amend_contact_email():
      
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email="Alice@ua", address = "US, NY, Washington ave., 1126"
    )
    c.amend_contact_email(new_email = "ALICE@com.ua")
    assert c.email == "ALICE@com.ua"

    #print(c)
#test_amend_contact_email()


def test_amend_contact_address():
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )
    c.amend_contact_address(new_address = 'UA, KYIV, Shevchenka blvd, 121 - B')
    assert c.address == 'UA, KYIV, Shevchenka blvd, 121 - B'

    #print(c)
#test_amend_contact_address()

def test_full_name():
    c = Contact("Alice", "Smith")
    result = (c.full_name() == "Alice Smith")
    assert result
    #print(result)

#test_full_name()

    
def test__eq__():
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )
    c1 = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )
    result = (c == c1)
    #assert result 
    #print(result)

#test__eq__()


def test_format_contact():
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )

    result = (c.format_contact() == 'Alice Smith : mobile - 123, work - 234, home - 345, Alice@ua, US, NY, Washington ave., 1126')
    assert result    
    #print(result)
    
#test_format_contact()


def test__str__():
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )

    result = (c.__str__() == 'Alice Smith : mobile - 123, work - 234, home - 345, Alice@ua, US, NY, Washington ave., 1126')
    assert result
    print(result)

test__str__()


def test__repr():
    c = Contact(
        "Alice", "Smith", mobile="123", work="234", home="345",
        email='Alice@ua', address = "US, NY, Washington ave., 1126"
    )

    expected = (
        "Contact(first='Alice', second='Smith', "
        "numbers=[('mobile', '123'), ('work', '234'), ('home', '345')], "
        "email='Alice@ua', address='US, NY, Washington ave., 1126')"
        )
    
    result = (repr(c) == expected)
    assert result
    print(result)
    
test__repr()

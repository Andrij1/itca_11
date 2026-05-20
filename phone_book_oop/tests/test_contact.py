import sys
sys.path.append('../')

from contact import Contact


def test_contact_name_create():
    c = Contact("Alice", "Smith")

    assert c.firstname == "Alice"
    assert c.lastname == "Smith"


def test_numbers_create():
    c = Contact(
        firstname=None,
        lastname=None,
        mobile="123",
        work="234",
        home="345"
    )

    assert ("mobile", "123") in c.numbers
    assert ("work", "234") in c.numbers
    assert ("home", "345") in c.numbers


def test_amend_contact_name():
    c = Contact("Alice", "Smith")

    c.amend_contact_name("SEAN")
    c.amend_contact_name(new_lastname="CONNARY")

    assert c.firstname == "SEAN"
    assert c.lastname == "CONNARY"


def test_amend_contact_email():
    c = Contact("Alice", "Smith", email="Alice@ua")

    c.amend_contact_email("ALICE@com.ua")
    assert c.email == "ALICE@com.ua"


def test_amend_contact_address():
    c = Contact("Alice", "Smith", address="old")

    c.amend_contact_address("UA, KYIV")
    assert c.address == "UA, KYIV"


def test_full_name():
    c = Contact("Alice", "Smith")

    assert c.full_name() == "Alice Smith"


def test__eq__():
    c = Contact("Alice", "Smith", email="a")
    c1 = Contact("Alice", "Smith", email="a")

    assert c == c1


def test_format_contact():
    c = Contact("Alice", "Smith", mobile="123", work="234", home="345",
                email="Alice@ua", address="NY")

    result = c.format_contact()

    assert "Alice Smith" in result
    assert "mobile - 123" in result


def test__str__():
    c = Contact("Alice", "Smith")

    assert str(c) == "Alice Smith"


def test__repr():
    c = Contact("Alice", "Smith", mobile="123")

    r = repr(c)

    assert "Alice" in r
    assert "Smith" in r

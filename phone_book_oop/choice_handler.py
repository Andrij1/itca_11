from cli import CliBook


def show_menu():
    start = input(
        '\n-> Enter "Y/y" - to print MENU :\n-> '
    ).strip().upper()
    if start != 'Y':
        print('\nmake your choice\n', "-" * 75, sep='')
        #continue

    choice = input(
        '\n            MENU :'
        '\n"1" - print the phone book \n'
        '"2" - search the phone book \n'
        '"3" - edit first (second) name in contact \n'
        '"4" - edit phone numbers in contact \n'
        '"5" - edit email in contact \n'
        '"6" - edit address in contact \n'
        '"7" - delete an entire contact \n'
        '"8" - add a new contact \n'
        '"9" - start the new phone book \n'
        '"QS/qs" - quit and save book contacts changes \n'
        '"0" - quit without save \n\n'
        '-> Enter your choice :\n-> ')

    print("-" * 75)
    return choice


def print_book(phonebook):
    if phonebook.book:
        for contact in phonebook.list_contacts():
            print(contact)
    else:
        print('\n-> No book exists yet - create a contact first')


def search_contact(phonebook):
    while True:
        contact, firstname, lastname = phonebook.find_contact()
        confirm = input(
            '\n"Q/q" - quit search, "ANY" - continue :\n-> '
        )
        if confirm.strip().upper() == 'Q':
            break


def edit_name(phonebook):
    while True:
        contact, firstname, lastname = phonebook.find_contact()
        if contact is None:
            break
        new_firstname = input(
            'Enter the new firstname :\n-> '
            ).strip()
        new_lastname = input(
            'Enter the new lastname :\n-> '
            ).strip()
        if not new_firstname or not new_lastname:
            print('fill the name fields')
            break
        contact.amend_contact_name(new_firstname, new_lastname)
        print(contact)
        confirm = input(
            '\n"Q/q" - quit editing, "ANY" - continue :\n-> '
            )
        if confirm.strip().upper() == 'Q':
            break


def edit_numbers(phonebook):
    while True:
        contact, firstname, lastname = phonebook.find_contact()
        if contact is None:
            break
        try:
            new_mobile = input(
                'Enter the new mobile # :\n-> '
            ).strip()
            new_work = input(
                'Enter the new work # :\n-> '
            ).strip()
            new_home = input(
                'Enter the new home # :\n-> '
            ).strip()
            n_updates = {
                'mobile': new_mobile,
                'work': new_work,
                'home': new_home
            }
            contact.amend_contact_number(n_updates)
            print(contact)
        except ValueError as e:
            print(e)

        confirm = input(
            '\n"Q/q" - quit editing, "ANY" - continue :\n-> '
        )
        if confirm.strip().upper() == 'Q':
            break


def edit_email(phonebook):
    while True:
        contact, firstname, lastname = phonebook.find_contact()
        if contact is None:
            break
        try:
            new_email = input('Enter the new email :\n-> ').strip()
            contact.amend_contact_email(new_email)
            print(contact)
        except ValueError as e:
            print(e)

        confirm = input(
            '\n"Q/q" - quit editing, "ANY" - continue :\n-> '
        )
        if confirm.strip().upper() == 'Q':
            break


def edit_address(phonebook):
    while True:
        contact, firstname, lastname = phonebook.find_contact()
        if contact is None:
            break
        try:
            new_address = input(
                'Enter the new address :\n-> '
            ).strip()
            contact.amend_contact_address(new_address)
            print(contact)
        except ValueError as e:
            print(e)

        confirm = input(
            '\n"Q/q" - quit editing, "ANY" - continue :\n-> '
        )
        if confirm.strip().upper() == 'Q':
            break


def delete_contact(phonebook):
    while True:
        contact, firstname, lastname = phonebook.find_contact()
        if contact is None:
            break
        try:
            confirm = input(
                '\n"Y/y" - confirm deleting, "ANY" - continue :\n-> '
            )
            if confirm.strip().upper() == 'Y':
                phonebook.remove_contact(contact)
                print('-> Contact deleted :\n ', contact)
        except ValueError as e:
            print(e)

        confirm = input(
            '\n"Q/q" - quit editing, "ANY" - continue :\n-> '
        )
        if confirm.strip().upper() == 'Q':
            break


def add_contact(phonebook):
    if phonebook.book:
        phonebook_cli = CliBook()
        while True:
            print('Check if the contact does not exist')
            contact, firstname, lastname = phonebook.find_contact()
            if contact is not None:
                print('The contact exists')
                break
            else:
                print('\n-> Contact not found - create the contact')

                contact = phonebook_cli.create_contact_cli(
                    firstname, lastname)
                phonebook.add_contact(contact)
                print(contact)

            confirm = input(
                '\n"Q/q" - quit contact constructor, "ANY" - continue :\n-> '
            )
            if confirm.strip().upper() == 'Q':
                break


def start_book(phonebook):
    if phonebook.book:
        confirm = input(
            'The Phonebook exists: "Y/y" - start new, "ANY" - quit :\n->  '
        ).strip().upper()
        if confirm != 'Y':
            return
        phonebook.book = []
    phonebook_cli = CliBook()

    while True:
        phonebook_cli.add_contact_cli(phonebook)
        confirm = input(
            '\n"Q/q" - quit book, "ANY" - continue :\n-> '
        ).strip().upper()
        if confirm.strip().upper() != 'Q':
            continue
        else:
            break


def quit_book(phonebook):
    print('Quit without trace')

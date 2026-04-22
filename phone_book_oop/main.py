from contact import Contact
from book import PhoneBook
from converters import JsonConverter, CSVConverter, DBConverter
from storages import MultiStorage, JsonStorage, CSVStorage, DBStorage
from cli import CliBook
from finder import find_contact


def main():       

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

    while True:
        start = input(
            '\n-> Enter "Y/y" - to print MENU :\n-> '
            ).strip().upper()
        if start != 'Y':
            print('\nmake your choice\n', "-" * 75, sep='')
            continue

        choice = input('\n            MENU :'
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

        if choice == '1':            
            if phonebook: 
                for contact in phonebook.list_contacts():
                    print(contact)                    
            else:
                print('\n-> No book exists yet - create a contact first')                    

        elif choice == '2':
            while True:
                contact, firstname, lastname = find_contact(phonebook)
                confirm = input(
                    '\n"Q/q" - quit search, "ANY" - continue :\n-> '
                    )
                if confirm.strip().upper() == 'Q':
                    break

        elif choice == '3':
            while True:
                contact, firstname, lastname = find_contact(phonebook)
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
                contact.amend_contact_name(new_firstname,new_lastname)
                print(contact)
                confirm = input(
                    '\n"Q/q" - quit editing, "ANY" - continue :\n-> '
                    )
                if confirm.strip().upper() == 'Q':
                    break

        elif choice == '4':
            while True:
                contact, firstname, lastname = find_contact(phonebook)
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

        elif choice == '5':
            while True:
                contact, firstname, lastname = find_contact(phonebook)
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

        elif choice == '6':
            while True:
                contact, firstname, lastname = find_contact(phonebook)
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
                
        elif choice == '7':
            while True:
                contact, firstname, lastname = find_contact(phonebook)
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
                
        elif choice == '8':
            if phonebook.book:
                phonebook_cli = CliBook()
                while True:
                    print('Check if the contact does not exist')
                    contact, firstname, lastname = find_contact(phonebook)
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

        elif choice == '9':
            if phonebook.book:
                confirm = input(
                    'The Phonebook exists: "Y/y" - start new, "ANY" - quit :\n->  '
                    ).strip().upper()
                if confirm != 'Y':
                    continue
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

        elif choice.strip().upper() == 'QS':
            storages.write(phonebook.list_contacts())
            print('Phonebook updated')
            break

        elif choice == '0':
            print('Quit without trace')
            break

        print('\n-> Make your choice ...')
        continue
    

if __name__ == '__main__':
    main()


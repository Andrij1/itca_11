from helper_phone_book_A_Panchenko import (
    read_book_as_json,
    write_book_as_json,
    create_contact,
    add_contact,
    create_contact_cli,
    add_contact_cli,
    create_phone_book_cli,
    find_contact_by,
    remove_contact,
    update_contact_first_name,
    update_contact_second_name,
    update_contact_number,
    display_contact,
    display_book
    )

def run():
    filename = "phone_book.json"    
    
    try:        
        book = read_book_as_json(filename)
        if book is None:
            book = []
    except FileNotFoundError:
        book = []
        print('File Not Found Error')

    phone_book_loaded = sorted([c for c in book if c is not None], key=lambda x: x['second_name'])
    
    while True:    

    
        choice = input('\n            MENU :'
                       '\n"1" - print the phone book \n'
                       '"2" - search the phone book \n' 
                       '"3" - edit first name in contact \n'
                       '"4" - edit second name in contact \n'
                       '"5" - edit phone numbers in contact \n'
                       '"6" - delete an entire contact \n'
                       '"7" - add a new contact \n'
                       '"8" - start the new phone book \n'                       
                       '"Q" - quit the phone book \n'
                       '"ANY" - press any key to continue \n\n' 
                       '--> Enter your choice: ')
        print("-" * 75)        

        if choice == '1':
            display_book(phone_book_loaded)

        elif choice == '2':
            display_book(phone_book_loaded)                
            search_by_input = input(
                    f'--> Enter value to find contacts: '
                    f'\n"1"-first name,"2"-second name,"3"-phone number : '
                    ).strip()
            if search_by_input == '1':
                search_by = 'first_name'                    
            elif search_by_input == '2':
                search_by = 'second_name'                    
            elif search_by_input == '3':
                search_by = 'numbers'
            try:                    
                search_value = input(
                        f'--> Enter the search item (name, number) : '
                        )
                contact = find_contact_by(phone_book_loaded, search_by,
                                              search_value)            
                display_contact(contact)
            except UnboundLocalError as err:
                print(err)
                continue                
            
            confirm = input(
                            '\nTo Continue - enter "Y", "ANY" - Exit to MENU: '
                            ).strip().upper()
            if confirm != 'Y':
                print("-" * 75)
                continue                                  

        elif choice == '3':
            if phone_book_loaded:
                display_book(phone_book_loaded)
                search_by_f_name='first_name'
                search_f_name = input(
                    f'--> Enter {search_by_f_name} to be changed in contacts: '
                    ).strip()
                contact_found = find_contact_by(book, search_by_f_name,
                                                search_f_name)
                if not contact_found:
                    print('\nContact not found!')
                    continue
                new_f_name = input(f'--> Enter a new {search_by_f_name}: ').strip()       
                
                confirm = input('--> Confirm first name edit- Y/ ANY - Quit: ').upper()
                if confirm != 'Y':
                    print('\nNo changes made!')
                    continue                 
                
                updated_f_name = update_contact_first_name(
                            phone_book_loaded, search_by_f_name, search_f_name,
                            new_f_name
                            )
                if updated_f_name:
                    write_book_as_json(phone_book_loaded, filename)
                    print(f'\n--> Changed the {search_by_f_name} in\n')
                    display_contact(updated_f_name)
                    continue      

        elif choice == '4':
            if phone_book_loaded:
                display_book(phone_book_loaded)  
                search_by_s_name='second_name'
                search_s_name = input(
                    f'--> Enter {search_by_s_name} to be changed in contacts: '
                    ).strip()
                contact_found = find_contact_by(book, search_by_s_name,
                                                search_s_name)
                if not contact_found:
                    print('\nContact not found!')
                    continue
                new_s_name = input(f'--> Enter a new {search_by_s_name}: ').strip()       
                
                confirm = input('--> Confirm second name edit- Y/ ANY - Quit: ').upper()
                if confirm != 'Y':
                    print('\nNo changes made!')
                    continue                 
                
                updated_s_name = update_contact_second_name(
                            phone_book_loaded, search_by_s_name, search_s_name,
                            new_s_name
                            )
                if updated_s_name:
                    write_book_as_json(phone_book_loaded, filename)
                    print(f'\n--> Changed the {search_by_s_name} in\n')
                    display_contact(updated_s_name)
                    continue

        elif choice == '5':
            if phone_book_loaded:
                display_book(phone_book_loaded)
                search_by_s_name='second_name'
                search_s_name = input(
                    f'--> Enter {search_by_s_name} of the contact '
                    f'numbers to change in: '
                    ).strip()
                contact_found = find_contact_by(book, search_by_s_name,
                                                search_s_name)                
                if not contact_found:
                    continue
                idx_choice = int(input('--> Choose number to change - "1 or 2" : '))-1
                new_number = input('Enter new number : ').strip()
                numbers = contact.get('numbers', [])
                if not numbers:
                    print('\nNo numbers in the contact exist')
                    continue                  
                updated_number = update_contact_number(
                            phone_book_loaded, search_by_s_name, search_s_name,
                            idx_choice, numbers, new_number)
                if updated_number:                    
                    write_book_as_json(phone_book_loaded, filename)
                    print(f'\n--> Changed the number in')
                    display_contact(updated_number)
                    continue

        elif choice == '6':
            if phone_book_loaded:
                display_book(phone_book_loaded)
                search_by_s_name='second_name'
                search_s_name = input(
                    f'--> Enter {search_by_s_name} of the contact '
                    f' to remove contact: '
                    ).strip()                
                remove_contact(phone_book_loaded, search_by_s_name,
                               search_s_name)
                write_book_as_json(phone_book_loaded, filename)
                print("-" * 75)           
                display_book(phone_book_loaded)                

        elif choice == '7':
            if phone_book_loaded:
                display_book(phone_book_loaded)
                contact_added = add_contact_cli(phone_book_loaded)
                if contact_added:
                    write_book_as_json(phone_book_loaded, filename)
                    print(f'\n--> Contact added')
                    display_contact(contact_added)
                      
        elif choice == '8':
            if phone_book_loaded:
                confirm = input('\nThe book EXISTS, enter Y/ ANY to start NEW/ Quit: ').upper()
                if confirm != 'Y':
                    continue
            phone_book_loaded = create_phone_book_cli()
            write_book_as_json(phone_book_loaded, filename)            
            display_book(phone_book_loaded)
            
        elif choice.upper() == 'Q':
            return
        

def tests():        
    filename = "phone_book_tests.json"
    book = read_book_as_json(filename)
    contact = [d for d in book]
    for contact in book:
        numbers = contact.get('numbers', [])
    
# ---------- create contact() test 
    new_contact = create_contact(first_name='Dunkan',
                                second_name ='Mcloud',
                                numbers=[('mobile', '+01010101'),
                                      ('mobile', '+10101010')])
    add_contact(book, new_contact)
    try:
        assert new_contact in book
    except:
        print(f'contact {new_contact} was not added')
        
# ---------- search contact() test
    f_contact = find_contact_by(book, search_by='first_name',
                                search_value='Dunkan')
    
    assert f_contact == new_contact
    
# ---------- update contact number() test
    new_number = '0000-0000-0001'
    updated_number = update_contact_number(
                    book, numbers, search_by_s_name='second_name',
                    search_s_name = 'Mcloud', idx_choice = 1, 
                    new_number = new_number)
    print()
    assert updated_number['numbers'][1][1] == new_number

# ---------- remove contact() test  - commented for printing results
    search_by_s_name='second_name'
    search_s_name = 'Mcloud'
    removed = remove_contact(book, search_by_s_name, search_s_name)
    print()
    assert removed is not None, "Contact not removed"
    assert removed not in book, "Removed contact still in book"
    assert all(c.get("second_name") != search_s_name for c in book)
    
# ---------- display contact() test
    display_contact(book[1])      
    assert book[1] is not None        



if __name__ == "__main__":    
    run_tests = False
    
    if run_tests:
        tests()
        
    run()

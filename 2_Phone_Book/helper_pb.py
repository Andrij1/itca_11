import json

# --------------------------------
# STORING BOOK FILE
# --------------------------------

def read_book_as_json(filename):
    try:
        with open(filename, "r") as book_file:
            return json.load(book_file)
    except FileNotFoundError:
        return []


def write_book_as_json(book, filename):
    with open(filename, "w") as book_file:
        json.dump(book, book_file, indent=2)   
    return book

# ---------------------------------
# CREATE, AMEND BOOK, CONTACT, FIND 
# ---------------------------------


def create_contact(first_name='', second_name ='', numbers=None):
    if numbers is None:
        numbers =  []
    return {
        'first_name': first_name.strip(),
        'second_name': second_name.strip(),
        'numbers': numbers
        }


def add_contact(book, contact):
    if contact is not None:
        book.append(contact)        
    return contact


def find_contact_by(book, search_by='', search_value = ''):
    search_value = search_value.strip()
    
    for contact in book:
        value = contact.get(search_by, '')
        if search_by != 'numbers':            
            if value and value.upper() == search_value.upper():
                return contact
        elif value and search_value in [number[1] for number in value]:
            return contact
        
    print(f'\n{"-" * 35}')
    print('\nThe contact is not found ')
    return None


def update_contact_first_name(book, search_by_f_name, search_f_name,
                              new_f_name):
    for contact in book:
        value = contact.get(search_by_f_name, '')       
        if search_f_name.upper() == value.upper():
            contact[search_by_f_name] = new_f_name
            print(f'{"-" * 35}')
            return contact
    return None


def update_contact_second_name(book, search_by_s_name, search_s_name,                               
                                new_s_name):
    for contact in book:
        value = contact.get(search_by_s_name, '')       
        if search_s_name.upper() == value.upper():
            contact[search_by_s_name] = new_s_name
            print(f'{"-" * 35}')
            return contact
    return None   


def update_contact_number(book, numbers, search_by_s_name, search_s_name, idx_choice,
                          new_number):    
    for contact in book:
        value = contact.get(search_by_s_name, '')       
        if str(search_s_name.upper()) == str(value.upper()):
            if idx_choice < 0 or idx_choice >= len(numbers):
                print('\nWrong choice')
                continue           
            
            for idx, (marker, number) in enumerate(contact['numbers']):
                contact['numbers'][idx_choice] = (marker, new_number)
                print(f'{"-" * 35}')
                return contact
    return None


def remove_contact(book, search_by_s_name='', search_s_name=''):
    search_s_name = search_s_name.strip()
    removed = False
    
    for contact in book:
        value = contact.get(search_by_s_name, '')
        if value.upper() == search_s_name.upper():
            print(f'\n--> Removed from contacts:\n{contact}')
            book.remove(contact)
            removed = True
            break
    if not removed:
        print('Wrong input, enter a valid name')
        return None

    return book

# --------------------------------
# INTERACTIVE BOOK PART
# --------------------------------

def display_contact(contact):
    if not contact:
        print('--- No contact ---')
        return
    print(
        f'\n{contact["first_name"] + " " + contact["second_name"]:20}'
        f'- {contact["numbers"]}'        
        )

def display_book(book):
    if not book:
        print('--- No book ---')
        return
    for contact in book:
        display_contact(contact)
    print(f'\n--> The phone book - search or edit it!\n{"-" * 75}')


def create_contact_cli():
      
    first_name = input('Enter the first name: ').strip()
    second_name = input('Enter the second name: ').strip()
    number_1 = input('Enter the number 1 : ').strip()
    number_2 = input('Enter the number 2 : ').strip()        
    numbers = [('mobile', number_1), ('mobile', number_2)]
    if numbers is None:
        numbers =  []

    return create_contact(first_name, second_name, numbers)  
        

def add_contact_cli(book):
    while True:
        contact = create_contact_cli()
        if contact is not None:
            add_contact(book, contact)            
        confirm = input('Enter "Y" - continue, "ANY" - quit : ').upper()
        if confirm != "Y":
            return contact
        else:
            continue
        
    return contact


def create_phone_book_cli():
    book = []
    contact = add_contact_cli(book)
    
    return book

    

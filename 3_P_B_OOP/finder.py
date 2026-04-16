
def find_contact(phonebook):
    
    firstname = input('Enter firstname :\n-> ').strip()
    lastname = input('Enter lastname :\n-> ').strip()
    found = phonebook.find_contact(firstname, lastname)
    
    if found:
        try:
            for i,c in enumerate(found):
                print(f'index - {i} : {c}')
            idx = int(input('Enter needed contact index :\n -> '))
            contact = found[idx]

            return contact, firstname, lastname
        except ValueError as e:
            print(e)
            return None, firstname, lastname
    else:
        print('\n-> Contact not found')
        return None, firstname, lastname
        


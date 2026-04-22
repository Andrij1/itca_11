from contact import Contact


class CliBook:

    def __init__(self):
        self.cli_book = []
        

    def create_contact_cli(self, firstname = None, lastname = None):

        if firstname is None:              
            self.firstname = input('Enter the first name: ').strip()
        else:
            self.firstname = firstname
        if lastname is None: 
            self.lastname = input('Enter the second name: ').strip()
        else:
            self.lastname = lastname
            
        self.mobile = input('Enter the mobile number : ').strip()
        self.work = input('Enter the work number: ').strip()
        self.home = input('Enter the home number: ').strip()        
        self.email = input('Enter the email: ').strip()
        self.address = input('Enter the address: ').strip()

        return Contact(
            self.firstname,
            self.lastname,
            self.mobile,
            self.work,
            self.home,
            self.email,
            self.address
            )  
        

    def add_contact_cli(self, phonebook):
        while True:
            self.contact = self.create_contact_cli()
            if self.contact is not None:
                phonebook.add_contact(self.contact)

            confirm = input('"Q/q" - quit contact, "ANY" - continue :\n-> ').strip().upper()
            if confirm != 'Q':
                continue
            else:
                break
                
        return self.contact


    def create_phone_book_cli(self):    
        self.add_contact_cli(phonebook)
        
        return phonebook.book

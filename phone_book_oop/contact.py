class Contact:
    
    def __init__(self, firstname, lastname, mobile=None, work=None, home=None, email=None, address=None):
        self.firstname = firstname     
        self.lastname = lastname       
        self.set_numbers(mobile, work, home)
        self.email = email
        self.address = address
        self.to_write = False


    def set_numbers(self, mobile=None, work=None, home=None):
        self.numbers = []
        if mobile:
            self.numbers.append(('mobile', mobile))
        if work:
            self.numbers.append(('work', work))
        if home:
            self.numbers.append(('home', home))            


    def amend_contact_name(self, new_firstname=None, new_lastname=None):
        changed = False
        if new_firstname is not None:
            self.firstname = new_firstname
            changed = True
            
        if new_lastname is not None:
            self.lastname = new_lastname
            changed = True

        if changed:
            self.to_write = True


    def amend_contact_number(self, n_updates=None):        
        if not n_updates:
            return
        
        valid_labels = ['mobile','work','home']
        changed = False

        for label, new_number in n_updates.items():
            if label not in valid_labels:
                continue
            if not new_number or new_number.upper() == 'Q':
                continue


            for i, (lbl, number) in enumerate(self.numbers):
                if lbl == label:
                    self.numbers[i] = (label, new_number)
                    changed = True
                    break
            else:
                self.numbers.append((label, new_number))
                changed = True

        if changed:
            self.to_write = True

 
    def amend_contact_email(self, new_email=None):
        if not new_email or new_email.upper() == 'Q':
            return        
        self.email = new_email
        self.to_write = True
      

    def amend_contact_address(self, new_address=None):
        if not new_address or new_address.upper() == 'Q':
            return
        self.address = new_address
        self.to_write = True
        
    
    def __eq__(self, other):
        if isinstance(other, Contact):
            return (
                self.firstname == other.firstname and
                self.lastname == other.lastname and
                self.numbers == other.numbers and
                self.email == other.email and
                self.address == other.address
            )
        
        if isinstance(other, dict):
            # dict must have all fields
            return (
                self.firstname == other.get("firstname") and
                self.lastname == other.get("lastname") and
                self.numbers == other.get("numbers", []) and
                self.email == other.get("email") and
                self.address == other.get("address")
            )
        
        return NotImplemented
            

    def full_name(self):
        return f'{self.firstname} {self.lastname}'
    

    def format_contact(self):        
        details = []
        
        valid_numbers = [(lbl, num) for lbl, num in self.numbers if lbl and num]
        if valid_numbers:
            details.append(', '.join(f'{lbl} - {num}' for lbl, num in valid_numbers))

        if self.email:
            details.append(self.email)

        if self.address:
            details.append(self.address)

        result = ', '.join(details)

        return f"{self.full_name()} : {result}" if result else self.full_name()

    
    def __str__(self):
        return self.format_contact()
    

    def __repr__(self):
        return (
                f"Contact(first={self.firstname!r}, second={self.lastname!r}, "
                f"numbers={self.numbers!r}, email={self.email!r}, address={self.address!r})"
                )
    

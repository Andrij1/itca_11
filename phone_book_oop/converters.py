from contact import Contact


class JsonConverter:    
    
    @staticmethod
    def to_dict(contact):
        return {
            "firstname": contact.firstname,
            "lastname": contact.lastname,
            "numbers": contact.numbers,
            "email": contact.email,
            "address": contact.address
        }
    
    
    @staticmethod
    def from_dict(data):
        contact = Contact(
            data["firstname"],
            data["lastname"],
            email=data.get("email"),
            address=data.get("address")
        )
        contact.numbers = [tuple(n) for n in data.get("numbers", [])]
        return contact


class CSVConverter:    

    @staticmethod
    def to_row(contact):
        numbers = ";".join(f"{lbl}:{num}" for lbl, num in contact.numbers)
        return [
            contact.firstname,
            contact.lastname,
            numbers,
            contact.email,
            contact.address
        ]
    

    @staticmethod
    def from_row(row):
        firstname, lastname, numbers, email, address = row
        numbers_list = []
        if numbers:
            for item in numbers.split(";"):
                lbl, num = item.split(":")
                numbers_list.append((lbl, num))

        contact = Contact(
                        firstname, lastname, email=email or None,
                        address=address or None
                        )
        contact.numbers = numbers_list
        return contact



class DBConverter:

    @staticmethod
    def to_list(contact):
        numbers = ','.join(f"{lbl}:{num}" for lbl, num in contact.numbers)
        contact_list = [
            contact.firstname,
            contact.lastname,
            numbers,
            contact.email,
            contact.address
            ]
        
        return contact_list    


    @staticmethod
    def from_list(line):
        firstname, lastname, numbers, email, address = line
        numbers_list = []
        if numbers: 
            for symb in [',', ';']:
                if symb in numbers:
                    for item in numbers.split(symb):
                        lbl, num = item.split(':')
                        numbers_list.append((lbl.strip(), num.strip()))
                    break
            else:                
                lbl, num = numbers.split(':')
                numbers_list.append((lbl.strip(), num.strip()))

        contact = Contact(
            firstname,
            lastname,
            email=email or None,
            address=address or None
            )
        contact.numbers = numbers_list
        
        return contact

from collections import UserDict

class Field:
    def __init__(self, value: str):
        self.value = value

class Name(Field):
    pass

class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phone: Phone = None):
        self.name = name
        if phone is not None:
            self.phone = [phone]
        else:
            self.phone = []

    def add_phone_field(self, phone_number: Phone):
        self.phone.append(phone_number)

    def change_phone_field(self, old_number: Phone, new_number: Phone):
        try: 
            self.phone.remove(old_number)
            self.phone.append(new_number)
        except ValueError:
            return f"Contact does not contain such phone number: {old_number}"
        
    def delete_phone_field(self, phone: Phone):
        try:
            self.phone.remove(phone)
        except ValueError:
            return f"Contact does not contain such phone number: {phone}"
        
class AddressBook(UserDict):

    def add_record(self, name : Name, phone: Phone = None):
        new_contact = Record(name=name, phone=phone)
        self.data[name.value] = new_contact
        
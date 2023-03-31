
import functools
from collections import UserDict

# decorators
def welcome(func):                                                     
    def inner(*args, **kwargs):
        print("-"*36+"\n  Welcome to Assistant Console Bot\n"+"-"*36)
        return func(*args, **kwargs)
    return inner


def error_input(func):                                                 
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except IndexError:
            print("""You have not entered all data!!!
--------------------------------------------------------------------------------------------------
for adding new phone number please input:   add name tel.      (example: add Denys 970-45-44)
for change please input:                    change name tel.   (example: change Denys 2345789)
for reading please input:                   phone name         (example: phone Denys)
--------------------------------------------------------------------------------------------------""")
        except KeyError:
            print("This user was not found in the phone book!")
        except ValueError:
            print("Invalid value. Try again.")
    return wrapper

# Classes
class Field:

    @ error_input
    def handler(self, enter_data):                                                        # функція обробки команд
        if enter_data.lower() == "hello":
            return "How can I help you?"
        
        if enter_data.lstrip()[0:3].lower() == "add":
            name = enter_data.split(" ")[1]
            phone = enter_data.split(" ")[2]
            address_book.add_data(name, phone)
            
        if "change" in enter_data.lower():
            name = enter_data.split(" ")[1]
            phone = enter_data.split(" ")[2]
            address_book.change_data(name, phone)
            
        if "phone" in enter_data.lower():
            return address_book.data[enter_data.split(" ")[1]]
        
        if "show all" in enter_data.lower():
            return address_book.show_all()
        
        return "Unknown command, please input correct data or command!"


class AddressBook(UserDict, Field):
    
    def show_all(self):
        if self.data == {}:
            my_string ="Your phone book is empty."
        else:
            my_string ="Display full phone book:\n"
            for key, value in address_book.data.items():
                my_string += ('{:<12} {:<15}\n'.format(key, ", ".join(value)))
        return my_string
    
    def change_data(self, name, phone):
        ph_list = self.data.get(name, [])
        ph_list[0] = phone
        self.data[name] = ph_list 

    def add_data(self ,name , phone = "", email = "" ):
        ph_list = self.data.get(name, [])
        ph_list.append(phone)
        self.data[name] = ph_list

class Name(Field):
    def __init__(self, name):
        self.name = name


class Phone(Field):
    def __init__(self, phone = ""):
        self.phone = phone


class Record(Field):
    def __init__(self ,name = "" , phone_list = [], email = ""):
        self.name = name
        self.phone_list = phone_list
        self.email = email


@ welcome
def main():
    while True:
        enter_data = input(": ")
        if enter_data.strip().lower() in [".", "good bye", "close", "exit", "stop", "palyanytsya"]:
            print("-"*36+"\n  Good bye!\n"+"-"*36)
            break
        else:
            print_me = field.handler(enter_data)
            if print_me != None:                                               
                print(print_me)
            continue

if __name__ == '__main__':
    address_book = AddressBook()
    record = Record()
    field = Field()
    main()
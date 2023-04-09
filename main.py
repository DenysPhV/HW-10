import functools
from classes import * 
CONTACTS_ARRAY = AddressBook()

def error_handler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
    # def wrapper(*args):
        result = False

        try:
            result = func(*args, **kwargs)
            # result = func(*args)
        except TypeError:
            print("""You have not entered all data!!!
--------------------------------------------------------------------------------------------------
for adding new phone number please input:   add name tel.      (example: add Denys 345-45-45)
for change please input:                    change name tel.   (example: change Denys 2345789)
for reading please input:                   phone name         (example: phone Denys)
--------------------------------------------------------------------------------------------------""")
        except KeyError:
            print("This user was not found in the phone book!")
        except ValueError:
            print("Invalid value. Try again.")
        except IndexError:
            print("Invalid value. Try again.")
        return result
    return wrapper


def welcome_bot(func):
    def inner(*args, **kwargs):
        print("-"*32+"\nWelcome to Assistant Console Bot\n"+"-"*32)
        return func(*args, **kwargs)
    return inner

#add name and number in dict
@error_handler
def attach(name: str, number: str):
    user_name = Name(name)
    phone = Phone(number)
    rec = Record(user_name, phone)
    
    if user_name in CONTACTS_ARRAY.keys():
      return f'Contact with name {name} already in the phone book'
    CONTACTS_ARRAY.add_record(rec)
    return f'Contact with name {name} and phone {number} add successful'
   
# change number contact
@error_handler
# def change(name:str, number:str):
#     if name not in COMMAND_ARRAY.keys():
#         raise KeyError
#     COMMAND_ARRAY[name] = number

def change(name: str, number:str):

    user_name = Name(name)
    phone = Phone(number)
    changed = Record(user_name, phone)

    old_phone = CONTACTS_ARRAY.get(user_name)
    if old_phone:
        CONTACTS_ARRAY.change_phone_field(changed)
        # CONTACTS_ARRAY[name] = phone
        return f'Phone for contact {name} successful changed'
    return f'In phone book no contact with name {name}'


def delete(name: str, number:str):

    phone = Phone(number)
    in_garbage = Record(phone)

    if phone in CONTACTS_ARRAY.values():
        return f'Contact with name {name} already in the phone book'
    CONTACTS_ARRAY.delete_phone_field(in_garbage)
    return f'Contact with name {name} and phone {number} deleted'


# take phone from dict 
@error_handler
def get_phone(name: str):
    return COMMAND_ARRAY[name]


# ask get phone give phone by name
@error_handler
def show_phone(name: str):

    look_phone = get_phone(name)
    if look_phone: 
        return look_phone
    

# read dict with contact
def reader():
    if not CONTACTS_ARRAY:
        return "Your contact list is empty."
    return CONTACTS_ARRAY.show_all()
    # array_message = ''
    # for name, number in CONTACTS_ARRAY.items():
    #     array_message += ('|{:<12}|{:<15}\n'.format(name, number))
    # return array_message

# say good bye and exit
@error_handler
def say_good_bye():
    return "Bye! Bye!"

def no_command(*args):
    return 'Unknown command. Try again'

COMMAND_ARRAY = {
    "hello": lambda: print("May I help you?"),
    "add": attach,
    "change": change,
    "phone": show_phone,
    "show all":reader,
    'exit': say_good_bye,
	'bye': say_good_bye,
	'quit': say_good_bye,
	'close': say_good_bye,
	'.': say_good_bye
}


@error_handler
def parser(command):
    for key in COMMAND_ARRAY.keys():
        if command.startswith(key):
            new_line = command[len(key):].title()
            return COMMAND_ARRAY[key], new_line.split()
    return no_command, []
            
@error_handler
def change_parser(name:str, number:str):
    if name not in COMMAND_ARRAY.keys():
        raise KeyError
    COMMAND_ARRAY[name] = number


@ welcome_bot
def main():
    while True:
        user_input = input("Please enter your command: ").lower().strip()
        command, data = parser(user_input)
        
        print(command(*data))
        
        if command == say_good_bye:
            break

if __name__ == "__main__":
    main()

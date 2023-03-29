from collections import UserDict


class Record:
	def __init__(self, name, phone=None):
		self.name = name
		self.phones = []

		if phone:
			self.add_phone(phone)

	def add_phone(self, phone):
		self.phones.append(phone)

	def update_phone(self, phone, new_phone):
		for i in range(len(self.phones)):
			if self.phones[i].value == phone.value:
				self.phones[i] = new_phone

	def delete_phone(self, phone):
		for i in range(len(self.phones)):
			if self.phones[i].value == phone.value:
				del self.phones[i]
				break


class Field:
	def __init__(self, value):
		self.value = value


class Name(Field):
	pass


class Phone(Field):
	pass


class AddressBook(UserDict):
	def add_record(self, record: Record):
		self.data[record.name.value] = record




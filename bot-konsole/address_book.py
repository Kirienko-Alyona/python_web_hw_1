from collections import UserDict
from record import Record
from datetime import datetime
from termcolor import colored
from print_table import header_func, line_func
import os
import pickle


class AddressBook(UserDict):

    def __init__(self):
        super().__init__()

        if os.path.exists("bot_name.bin") and os.path.getsize("bot_name.bin") > 0:
            with open("bot_name.bin", "rb") as b_name:
                self.bot_name = pickle.load(b_name)
        else:
            self.bot_name = "Jarvis"

    def add_record(self, record: Record) -> str:
        '''Adds name (key) of the contact and his fields (value).'''
        self.data[record.name.value] = record  # .title()
        return colored("New contact was added successfuly.", "green")

    def search_in_contact_book(self, data) -> str:
        '''Looks for mathches in names, phones, mails, tags, notes, birthdays.'''

        table = header_func()
        data = data[0] if data else ""
        counter = 0

        for name, record in self.data.items():

            phones = [phone.value for phone in record.phones]
            phones = " ".join(phones)
            emails = [email.value for email in record.emails]
            emails = " ".join(emails)
            birthday = record.birthday.value.strftime(
                "%m.%d.%Y") if record.birthday else ""
            tag = " ".join(record.tag.value if record.tag else "")
            note = record.note.value if record.note else ""

            if (
                data in name or
                data in birthday or
                data in emails or
                data in phones or
                data in tag or
                data in note
            ):

                table += line_func(record)
                counter += 1

        if counter < 1 and not data:
            return colored(f"The address book is emty.", "yellow")

        if counter < 1:
            return colored(f"I didn't find any '{data}' in adress book.", "yellow")

        return table

    def all_birthdays(self, range_days) -> list:
        '''Returns the list of all b-days in the next N-days.'''
        list_accounts = []

        for record_elem in self.data.values():

            if record_elem.birthday:
                days_to_next_birthday = record_elem.days_to_birthdays()

                if days_to_next_birthday <= range_days:
                    current_year = datetime.now().year
                    current_day = datetime.now()
                    this_year_birthday = datetime(
                        year=current_year, month=record_elem.birthday.value.month, day=record_elem.birthday.value.day)

                    if (this_year_birthday - current_day).days >= 0:
                        next_birth = this_year_birthday - current_day
                        return next_birth.days
                    else:
                        next_birth = datetime(
                            year=current_year + 1, month=record_elem.birthday.value.month, day=record_elem.birthday.value.day)
                    data = [record_elem.name.value.title(
                    ), next_birth.strftime("%A %d %B %Y")]
                    list_accounts.append(data)

            else:
                continue

        return list_accounts

    def delete_record(self, contact_name: str) -> str:
        '''Deletes the contact (key).'''
        self.data.pop(contact_name)
        return colored("The contact was deleted successfully.", "green")

    def save_address_book(self) -> str:
        '''Saves the address book.'''
        with open("address_book.bin", "wb") as file:
            pickle.dump(self.data, file)

    def load_address_book(self) -> str:
        '''Loads the address book.'''
        try:
            with open("address_book.bin", "rb") as file:
                self.data = pickle.load(file)
        except FileNotFoundError:
            return colored("The file does not exist.", "red")

    def change_bot_name(self, new_name: str) -> str:
        '''Changes the name of the bot.'''
        if new_name and new_name != self.bot_name:
            self.bot_name = new_name.title()
            with open("bot_name.bin", "wb") as file:
                pickle.dump(self.bot_name, file)
            return f"The bot's name was changed to {self.bot_name}."
        else:
            return f"Please enter the name or the bot already has this name."


address_book = AddressBook()
address_book.load_address_book()

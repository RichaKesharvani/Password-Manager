
import random
from tkinter import *


class PasswordGenerator:

    def __init__(self, password_entry):
        self.password_entry = password_entry

    def gen_password(self):

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_letters = [random.choice(letters) for _ in range(nr_letters)]
        password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

        password_list = password_letters + password_symbols + password_numbers

        random.shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.delete(0, END)

        self.password_entry.insert(0, password)




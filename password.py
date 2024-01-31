from random import randint, choice, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pw(password_input):
    pw_letters = [choice(letters) for n in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for n in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for n in range(randint(2, 4))]

    password_list = [*pw_letters, *pw_symbols, *pw_numbers]
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert("end", password)
    pyperclip.copy(password)

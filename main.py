from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

FONT_SIZE = 10


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def generate_pw():
    pw_letters = [choice(letters) for n in range(randint(8, 10))]
    pw_symbols = [choice(symbols) for n in range(randint(2, 4))]
    pw_numbers = [choice(numbers) for n in range(randint(2, 4))]

    password_list = [*pw_letters, *pw_symbols, *pw_numbers]
    shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(END, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    data = {"website": website, "email": email, "password": password}

    if validate(data):
        is_ok = messagebox.askokcancel(title="Confirming details",
                                       message=f"These are the details entered:\nWebsite: {website}\nEmail: {email}\n"
                                               f"Password: {password}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {password}\n")

            website_input.delete(0, "end")
            email_input.delete(0, "end")
            password_input.delete(0, "end")
    else:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty!")


def validate(data):
    website_len = len(data["website"])
    email_len = len(data["email"])
    password_len = len(data["password"])

    if website_len and email_len and password_len:
        return True
    else:
        return False


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=50, padx=50)

# ------------- Row 0 ------------- #
logo = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo.create_image(100, 100, image=logo_img)
logo.grid(row=0, column=1)

# ------------- Row 1 ------------- #
website_label = Label(text="Website:", font=("Arial", FONT_SIZE))
website_label.grid(row=1, column=0)

website_input = Entry(width=38)
website_input.grid(row=1, column=1, columnspan=2)
website_input.focus()

# ------------- Row 2 ------------- #
email_label = Label(text="Email/Username:", font=("Arial", FONT_SIZE))
email_label.grid(row=2, column=0)

email_input = Entry(width=38)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "youremail@email.com")

# ------------- Row 3 ------------- #
password_label = Label(text="Password:", font=("Arial", FONT_SIZE))
password_label.grid(row=3, column=0)

password_input = Entry(width=22)
password_input.grid(row=3, column=1)

password_btn = Button(text="Generate Password", padx=2, pady=2, font=("Arial", FONT_SIZE), command=generate_pw)
password_btn.grid(row=3, column=2)

# ------------- Row 4 ------------- #
add_btn = Button(text="Add", width=40, font=("Arial", FONT_SIZE), command=save)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()

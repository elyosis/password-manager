from tkinter import *
from password import generate_pw
from data_manager import save, find_website

FONT_SIZE = 10

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

website_input = Entry(width=24)
website_input.grid(row=1, column=1)
website_input.focus()

search_button = Button(text="Search", font=("Arial", FONT_SIZE), width=12, command=lambda: find_website(website_input))
search_button.grid(row=1, column=2)

# ------------- Row 2 ------------- #
email_label = Label(text="Email/Username:", font=("Arial", FONT_SIZE))
email_label.grid(row=2, column=0)

email_input = Entry(width=38)
email_input.grid(row=2, column=1, columnspan=2)
email_input.insert(0, "youremail@email.com")

# ------------- Row 3 ------------- #
password_label = Label(text="Password:", font=("Arial", FONT_SIZE))
password_label.grid(row=3, column=0)

password_input = Entry(width=24)
password_input.grid(row=3, column=1)

password_btn = Button(text="Create Password", padx=2, pady=2, font=("Arial", FONT_SIZE),
                      command=lambda: generate_pw(password_input))
password_btn.grid(row=3, column=2)

# ------------- Row 4 ------------- #
add_btn = Button(text="Add", width=40, font=("Arial", FONT_SIZE),
                 command=lambda: save(website_input, email_input, password_input))
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()

from tkinter import messagebox
import json
from validate import validate


# --- SAVE NEW DATA ---#


def save(website_input, email_input, password_input):
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    new_data = {website: {
        "email": email,
        "password": password}
    }

    if validate(new_data, website):
        try:
            with open("data.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            if website in data:
                is_overwritten = messagebox.askokcancel(title="Website already found",
                                                        message=f"{website} seems to have already been added. "
                                                                f"Overwrite data?")
                if not is_overwritten:
                    return
            data.update(new_data)
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_input.delete(0, "end")
            email_input.delete(0, "end")
            password_input.delete(0, "end")
    else:
        messagebox.showwarning(title="Error", message="Please don't leave any fields empty!")


# --- FIND SAVED DATA ---#


def find_website(website_input):
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showinfo(title="No Data File", message="No data has been saved yet.")
    else:
        website = website_input.get()
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Unsuccessful Search", message="No details for the website indicated exist.")

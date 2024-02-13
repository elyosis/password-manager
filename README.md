# Password Manager

A simple password manager GUI program made in Python with the `tkinter` module. Run `main.py` to start it.

When adding a new website, the program stores the data, unencrypted, in a JSON file; the credentials are stored in an object with the site's name as a key:

```json
"new_website": {
        "email": "your-email@email.com",
        "password": "(Hd1B*6bTWwP"
    }
  ```

By default, the file's name is `data.json` and, if it doesn't already exist upon using the program for the first time, it'll be created in the same directory as the program files. This can be changed by modifying the `DATA_PATH` variable in `config.py`.

The program can also generate a random password with 8-10 letters, 2-4 numbers and 2-4 symbols. The generated password is automatically copied to the user's clipboard for immediate use.

Finally, stored credentials can be retrieved from the program through the "Search" button by inputting the website name (search is case-sensitive).
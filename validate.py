def validate(data, website):
    website_len = len(data[website])
    email_len = len(data[website]["email"])
    password_len = len(data[website]["password"])

    if website_len and email_len and password_len:
        return True
    else:
        return False

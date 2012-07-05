import re

def valid_username(usr):
    usr_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return usr_re.match(usr)

def valid_password(pw):
    pw_re = re.compile("^.{3,20}$")
    return pw_re.match(pw)

def valid_email(email):
    email_re = re.compile("^[\S]+@[\S]+\.[\S]+$")
    return email_re.match(email)
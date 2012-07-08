import bcrypt

def hash_password(password, salt=None):
    if not salt:
        salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password, salt)
    return [hashed_pw, salt]

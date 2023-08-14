import bcrypt


def password_encrypt(password: str):
    hashed_pass = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed_pass.decode("utf-8")


def password_check(input_password: str, stored_password: str):
    return bcrypt.checkpw(input_password.encode('UTF-8'), stored_password.encode('UTF-8'))

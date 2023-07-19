import bcrypt


def password_encrypt(string: str):
    hashed_pass = bcrypt.hashpw(string.encode("utf-8"), bcrypt.gensalt())
    return hashed_pass.decode("utf-8")

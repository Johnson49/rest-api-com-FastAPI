from passlib.hash import pbkdf2_sha256


def generate_hash(password: str):
    return pbkdf2_sha256.hash(password)


def check_hash(password: str, hash: str):
    return pbkdf2_sha256.verify(password, hash)
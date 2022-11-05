from passlib.context import CryptContext


hash_context = CryptContext(schemes=['bcrypt'])

def generate_hash(password: str):
    return hash_context.hash(password)


def check_hash(password: str, hash: str):
    return hash_context.verify(password, hash)
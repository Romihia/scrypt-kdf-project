import os

def generate_random_salt(length=16) -> bytes:
    """
    Generates a random salt of a fixed length
    :param length: Salt length
    :return: Salt as a bytes sequence
    """
    return os.urandom(length)
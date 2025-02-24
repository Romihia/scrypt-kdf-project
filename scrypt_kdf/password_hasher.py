import os
import base64
from scrypt_kdf.key_derivation import derive_key

def generate_salt(length=16) -> bytes:
    """
    Generates a random salt value.
    :param length: Salt length (default 16 bytes)
    :return: Salt as a bytes sequence
    """
    return os.urandom(length)

def hash_password(password: str, salt: bytes) -> str:
    """
    Returns an encrypted hash of a password with a salt.
    :param password: Password to encrypt
    :param salt: Salt used in encryption
    :return: Base64-encoded string containing the hash
    """
    key = derive_key(password, salt)
    return base64.b64encode(salt + key).decode()

def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verifies a password against a stored hash.
    :param password: Password to verify
    :param hashed_password: Stored hash to compare against
    :return: True if the password matches, False otherwise
    """
    decoded = base64.b64decode(hashed_password)
    salt = decoded[:16]  # First part is the salt
    stored_key = decoded[16:]  # Second part is the hash
    return stored_key == derive_key(password, salt)
import hashlib

def derive_key(password: str, salt: bytes, n=16384, r=8, p=1, dklen=32) -> bytes:
    """
    Derives a cryptographic key from a password using Scrypt
    :param password: Plaintext password
    :param salt: Random salt value
    :param n: CPU/memory cost parameter (default 16384)
    :param r: Block size
    :param p: Parallelization factor
    :param dklen: Desired key length (default 32 bytes)
    :return: Encrypted key as bytes
    """
    key = hashlib.scrypt(password.encode(), salt=salt, n=n, r=r, p=p, dklen=dklen)
    return key
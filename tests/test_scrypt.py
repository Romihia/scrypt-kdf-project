import unittest
import base64
import sys
import os
import binascii
import hashlib

# Ensure the module is found
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scrypt_kdf.password_hasher import hash_password, verify_password, generate_salt

class TestScryptKDF(unittest.TestCase):

    def test_scrypt_key_derivation(self):
        password = "securepassword"
        salt = generate_salt()
        hashed_pw = hash_password(password, salt)
        self.assertTrue(verify_password(password, hashed_pw))

    def test_scrypt_invalid_password(self):
        password = "securepassword"
        wrong_password = "wrongpassword"
        salt = generate_salt()
        hashed_pw = hash_password(password, salt)
        self.assertFalse(verify_password(wrong_password, hashed_pw))


if __name__ == '__main__':
    unittest.main()

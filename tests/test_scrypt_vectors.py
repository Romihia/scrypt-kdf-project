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

    def test_scrypt_vectors(self):
        # Define test vectors from RFC 7914
        test_cases = [
            {
                "password": b"",
                "salt": b"",
                "N": 16,
                "r": 1,
                "p": 1,
                "dklen": 64,
                "expected": "77d6576238657b203b19ca42c18a0497f16b4844e3074ae8dfdffa3fede21442fcd0069ded0948f8326a753a0fc81f17e8d3e0fb2e0d3628cf35e20c38d18906"
            },
            {
                "password": b"password",
                "salt": b"NaCl",
                "N": 1024,
                "r": 8,
                "p": 16,
                "dklen": 64,
                "expected": "fdbabe1c9d3472007856e7190d01e9fe7c6ad7cbc8237830e77376634b3731622eaf30d92e22a3886ff109279d9830dac727afb94a83ee6d8360cbdfa2cc0640"
            },
            {
                "password": b"pleaseletmein",
                "salt": b"SodiumChloride",
                "N": 16384,
                "r": 8,
                "p": 1,
                "dklen": 64,
                "expected": "7023bdcb3afd7348461c06cd81fd38ebfda8fbba904f8e3ea9b543f6545da1f2d5432955613f0fcf62d49705242a9af9e61e85dc0d651e40dfcf017b45575887"
            }
        ]

        # Run each test case
        for test in test_cases:
            derived_key = hashlib.scrypt(
                password=test["password"],
                salt=test["salt"],
                n=test["N"],
                r=test["r"],
                p=test["p"],
                dklen=test["dklen"]
            )

            # Convert to hexadecimal string and compare with expected
            derived_key_hex = binascii.hexlify(derived_key).decode()
            self.assertEqual(derived_key_hex, test["expected"], f"Failed for: {test}")


if __name__ == '__main__':
    unittest.main()

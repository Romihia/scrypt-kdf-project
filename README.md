
### Scrypt Key Derivation Function (KDF)

## **Overview**
This project implements the **Scrypt Key Derivation Function (KDF)**, a secure way to derive cryptographic keys from passwords. It is designed to protect against brute-force attacks by making key derivation computationally and memory-intensive.

Scrypt is commonly used for:
- Secure **password hashing**
- **Key derivation** for cryptographic applications
- Protecting **against GPU and ASIC-based attacks**

---

## **Installation & Usage**

### **Step 1: Install Dependencies**
Make sure you have Python installed, then install the required packages:
```bash
pip install -r requirements.txt
```

---

### **Step 2: Run the Main Script**
To generate and verify password hashes, start the main script:
```bash
python main.py
```
This will prompt you to enter a password, generate a hashed version, and allow verification.

---

### **Step 3: Run the Tests**
Ensure that the implementation works correctly by running the test suite:
```bash
pytest tests/
```
This runs unit tests, including official **RFC 7914 test vectors**, to validate the correctness of the Scrypt implementation.


from scrypt_kdf.password_hasher import hash_password, verify_password, generate_salt

def main():
    password = input("Enter a password: ")
    
    # Generate a new salt and encrypt the password
    salt = generate_salt()
    hashed_password = hash_password(password, salt)
    print(f"Encrypted password: {hashed_password}")
    
    # Verify password
    verify = input("Verify password (enter again): ")
    if verify_password(verify, hashed_password):
        print("Password is correct!")
    else:
        print("Incorrect password!")

if __name__ == "__main__":
    main()
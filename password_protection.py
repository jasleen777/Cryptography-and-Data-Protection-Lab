
import os
import hashlib
import hmac
import getpass

# Step 1: Ask the user to create a password
password = getpass.getpass("Create your password: ")

# Step 2: Generate a random salt
salt = os.urandom(16)

# Step 3: Generate a secure password hash
password_hash = hashlib.pbkdf2_hmac(
    "sha256",
    password.encode(),
    salt,
    600000
)

print("\nPassword has been securely stored as a hash.")

# Step 4: Ask the user to enter the password again
entered_password = getpass.getpass("Enter your password to log in: ")

# Step 5: Generate a hash of the entered password
entered_hash = hashlib.pbkdf2_hmac(
    "sha256",
    entered_password.encode(),
    salt,
    600000
)

# Step 6: Compare both hashes
if hmac.compare_digest(password_hash, entered_hash):
    print("Login successful! Correct password.")
else:
    print("Login failed! Incorrect password.")

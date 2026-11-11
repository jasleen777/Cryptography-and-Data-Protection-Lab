
from cryptography.fernet import Fernet

# Step 1: Generate an encryption key
key = Fernet.generate_key()

# Step 2: Create a cipher using the key
cipher = Fernet(key)

# Step 3: Original message
message = "My confidential information"

# Step 4: Convert message into bytes and encrypt it
encrypted_message = cipher.encrypt(message.encode())

# Step 5: Decrypt the encrypted message
decrypted_message = cipher.decrypt(encrypted_message).decode()

# Step 6: Display the results
print("Original Message:", message)
print("Encryption Key:", key)
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message)



import hashlib

# Step 1: Create an original message
message = "My confidential information"

# Step 2: Convert the message into bytes
message_bytes = message.encode()

# Step 3: Generate SHA-256 hash
hash_object = hashlib.sha256(message_bytes)

# Step 4: Convert hash into hexadecimal format
hash_value = hash_object.hexdigest()

# Step 5: Display the results
print("Original Message:", message)
print("SHA-256 Hash:", hash_value)
print("Length of Hash:", len(hash_value))

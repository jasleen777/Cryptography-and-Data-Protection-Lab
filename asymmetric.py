
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.exceptions import InvalidSignature

# Step 1: Generate a private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Step 2: Generate the matching public key
public_key = private_key.public_key()

# Step 3: Create an original message
message = b"This is my confidential message."

# Step 4: Encrypt using the public key
encrypted_message = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# Step 5: Decrypt using the private key
decrypted_message = private_key.decrypt(
    encrypted_message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

print("Original Message:", message.decode())
print("Encrypted Message:", encrypted_message)
print("Decrypted Message:", decrypted_message.decode())

# Step 6: Create a digital signature using the private key
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature Created Successfully!")

# Step 7: Verify the signature using the public key
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verified! Message is authentic.")

except InvalidSignature:
    print("Signature Verification Failed!")

# Step 8: Test with a changed message
changed_message = b"This is a changed message."

try:
    public_key.verify(
        signature,
        changed_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Signature Verified!")

except InvalidSignature:
    print("Tampering Detected! Signature is invalid.")

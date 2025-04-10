from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization

private_key = rsa.generate_private_key(public_exponent=65537, key_size=1024)
public_key = private_key.public_key()

message = input("Enter the message to sign: ").encode()

signature = private_key.sign(
    message,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)

print("\n🔐 Signature (in hex):", signature.hex())
print("📤 Sending Message + Signature to Receiver...\n")

received_message = input("Receiver - Enter the received message: ").encode()

try:
    public_key.verify(
        signature,
        received_message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    print("✅ Signature Verified - Message is Authentic.")
except Exception as e:
    print("❌ Signature Invalid - Message Tampered or Not from Sender.")

import hashlib
def generate_hash(message):
    return hashlib.sha256(message.encode()).hexdigest()
message = input("Enter the message: ")
digest = generate_hash(message)
print("Generated SHA-256 Digest:", digest)
received_message = input("\nReceiver - Enter the received message: ")
received_digest = generate_hash(received_message)
if received_digest == digest:
    print("✅ Message is authentic (Digest matched)")
else:
    print("❌ Message has been tampered (Digest mismatch)")

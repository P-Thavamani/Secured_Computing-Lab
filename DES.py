from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Use a fixed 8-byte key
key = "thavaman".encode()

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_CBC, iv=b'12345678')  # Fixed 8-byte IV
    ciphertext = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_CBC, iv=b'12345678')
    return unpad(cipher.decrypt(ciphertext), DES.block_size).decode()

# Example Usage
plaintext = "Hello, DES!"
ciphertext = des_encrypt(plaintext, key)
decrypted_text = des_decrypt(ciphertext, key)

print("Ciphertext:", ciphertext.hex())  
print("Decrypted Text:", decrypted_text)

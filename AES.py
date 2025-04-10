from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def fix_key(key):
    return key.ljust(16, '0')[:16].encode()  # Ensures 16 bytes (128-bit)

def aes_encrypt(plaintext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b'1234567890123456')
    return cipher.encrypt(pad(plaintext.encode(), AES.block_size))

def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_CBC, iv=b'1234567890123456')
    return unpad(cipher.decrypt(ciphertext), AES.block_size).decode()

key = fix_key(input("Enter the Key: "))
plaintext = input("Enter the Text: ")

ciphertext = aes_encrypt(plaintext, key)
decrypted_text = aes_decrypt(ciphertext, key)

print("Ciphertext:", ciphertext.hex())  
print("Decrypted Text:", decrypted_text)

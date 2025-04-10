import base64

def vernam_encrypt(text, key):
    if len(text) != len(key):
        raise ValueError("Key length must match text length!")
    return bytes([ord(text[i]) ^ ord(key[i]) for i in range(len(text))])

def vernam_decrypt(ciphertext, key):
    return ''.join(chr(ciphertext[i] ^ ord(key[i])) for i in range(len(ciphertext)))

text = input("Enter the text: ")
key = input("Enter the key (same length as text): ")

if len(text) != len(key):
    print("Error: Key length must be the same as the text length!")
else:
    cipher = vernam_encrypt(text, key)
    cipher_hex = cipher.hex()
    decrypted_text = vernam_decrypt(cipher, key)

    print("Encrypted (Hex):", cipher_hex)  
    print("Encrypted (Base64):", base64.b64encode(cipher).decode())  
    print("Decrypted:", decrypted_text)

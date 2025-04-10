def vigenere_encrypt(text, key):
    key = key.upper()
    text = text.upper()
    encrypted = ""
    for i in range(len(text)):
        if text[i].isalpha():
            shift = ord(key[i % len(key)]) - 65
            encrypted += chr((ord(text[i]) - 65 + shift) % 26 + 65)
        else:
            encrypted += text[i]
    return encrypted

def vigenere_decrypt(ciphertext, key):
    key = key.upper()
    decrypted = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(key[i % len(key)]) - 65
            decrypted += chr((ord(ciphertext[i]) - 65 - shift) % 26 + 65)
        else:
            decrypted += ciphertext[i]
    return decrypted

text = input("Enter the Plain Text: ")
key = input("KEY : ")
cipher = vigenere_encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", vigenere_decrypt(cipher, key))

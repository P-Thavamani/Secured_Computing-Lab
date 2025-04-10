def monoalphabetic_cipher(text, key, decrypt=False):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    key = key.upper() 
    mapping = {key[i]: alphabet[i] for i in range(len(alphabet))} if decrypt else {alphabet[i]: key[i] for i in range(len(alphabet))}
    return ''.join(mapping[c] if c.isalpha() else c for c in text.upper())

plaintext = str(input("Enter the Plain Text :"))
key = str(input("Enter the Key : "))
encrypted = monoalphabetic_cipher(plaintext, key)
decrypted = monoalphabetic_cipher(encrypted, key, decrypt=True)

print("Original Text:", plaintext)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)

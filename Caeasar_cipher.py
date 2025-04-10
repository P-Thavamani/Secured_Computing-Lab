def caesar_encrypt(text, shift):
    return "".join(chr((ord(c) - 65 + shift) % 26 + 65) if c.isalpha() else c for c in text.upper())

def caesar_decrypt(ciphertext, shift):
    return "".join(chr((ord(c) - 65 - shift) % 26 + 65) if c.isalpha() else c for c in ciphertext)

text = "HELLO"
shift = 3
cipher = caesar_encrypt(text, shift)
print("Encrypted:", cipher)
print("Decrypted:", caesar_decrypt(cipher, shift))

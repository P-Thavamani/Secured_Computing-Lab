import numpy as np

def hill_encrypt(plain, key):
    key_size = int(len(key) ** 0.5)
    key_matrix = np.array([ord(c) - 65 for c in key]).reshape(key_size, key_size)
    plain = plain.upper().replace(" ", "") + 'X' * (-len(plain) % key_size)
    text_matrix = np.array([ord(c) - 65 for c in plain]).reshape(-1, key_size)
    return ''.join(chr(c % 26 + 65) for c in text_matrix @ key_matrix % 26)

def hill_decrypt(cipher, key):
    key_size = int(len(key) ** 0.5)
    key_matrix = np.array([ord(c) - 65 for c in key]).reshape(key_size, key_size)
    key_inv = np.round(np.linalg.inv(key_matrix) * np.linalg.det(key_matrix)).astype(int) % 26
    key_inv = (pow(int(round(np.linalg.det(key_matrix))) % 26, -1, 26) * key_inv) % 26
    text_matrix = np.array([ord(c) - 65 for c in cipher]).reshape(-1, key_size)
    return ''.join(chr(c % 26 + 65) for c in text_matrix @ key_inv % 26)

# Example Usage
plain_text = "HELLO"
key = "GYBNQKURP"  # 3x3 valid key

cipher_text = hill_encrypt(plain_text, key)
decrypted_text = hill_decrypt(cipher_text, key)

print("Encrypted:", cipher_text)
print("Decrypted:", decrypted_text)

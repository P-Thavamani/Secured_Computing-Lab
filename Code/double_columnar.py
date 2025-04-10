import numpy as np

def columnar_transpose_encrypt(text, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_rows = -(-len(text) // len(key))
    grid = np.full((num_rows, len(key)), 'X', dtype=str)

    for i, char in enumerate(text):
        grid[i // len(key), i % len(key)] = char

    ciphertext = "".join("".join(grid[:, i]) for i in key_order)
    return ciphertext

def columnar_transpose_decrypt(ciphertext, key):
    key_order = sorted(range(len(key)), key=lambda k: key[k])
    num_rows = -(-len(ciphertext) // len(key))
    grid = np.full((num_rows, len(key)), 'X', dtype=str)

    index = 0
    for i in key_order:
        for j in range(num_rows):
            if index < len(ciphertext):
                grid[j, i] = ciphertext[index]
                index += 1

    return "".join("".join(row) for row in grid).rstrip('X')

text = input("Enter the plain Text: ")
key = input("Enter the key: ")
cipher = columnar_transpose_encrypt(text, key)
print("Encrypted:", cipher)
print("Decrypted:", columnar_transpose_decrypt(cipher, key))

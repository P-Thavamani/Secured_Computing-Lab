def gcd(a, b):
    while b: a, b = b, a % b
    return a

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
    
def is_prime(n):
    return all(n % i != 0 for i in range(2, int(n**0.5)+1))

p = int(input("Enter first prime (p): "))
q = int(input("Enter second prime (q): "))

if not (is_prime(p) and is_prime(q)):
    print("Both numbers must be prime!")
    exit()

n = p * q
phi = (p - 1) * (q - 1)
e = 65537 if gcd(65537, phi) == 1 else 3
d = modinv(e, phi)

print(f"Public Key: (e={e}, n={n})")
print(f"Private Key: (d={d}, n={n})")

msg = input("Enter message (only letters): ").upper()

# Encrypt each character
cipher = [pow(ord(char), e, n) for char in msg]
print("Encrypted:", cipher)

# Decrypt each integer back to char
decrypted = ''.join([chr(pow(c, d, n)) for c in cipher])
print("Decrypted:", decrypted)

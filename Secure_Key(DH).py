import random
p = 23 
g = 5 

print(f"Public Parameters:\nPrime (p) = {p}\nPrimitive Root (g) = {g}\n")
a = random.randint(1, p - 1)
A = pow(g, a, p)
print(f"Alice's Private Key (a): {a}")
print(f"Alice's Public Key (A): {A}")
b = random.randint(1, p - 1)
B = pow(g, b, p)
print(f"\nBob's Private Key (b): {b}")
print(f"Bob's Public Key (B): {B}")
shared_secret_alice = pow(B, a, p)
shared_secret_bob = pow(A, b, p)

print(f"\nAlice's Computed Shared Secret: {shared_secret_alice}")
print(f"Bob's Computed Shared Secret:   {shared_secret_bob}")
if shared_secret_alice == shared_secret_bob:
    print(f"\n✅ Shared Secret Key Established: {shared_secret_alice}")
else:
    print("\n❌ Shared secrets don't match! Something went wrong.")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(n, phi_n):
    e = 1741
    d = mod_inverse(e, phi_n)
    return (e, n), (d, n)

def encrypt(message, public_key):
    e, n = public_key
    encrypted_message = pow(int.from_bytes(message.encode(), 'big'), e, n)
    return encrypted_message

def decrypt(encrypted_message, private_key):
    d, n = private_key
    decrypted_bytes = pow(encrypted_message, d, n)
    decrypted_message = decrypted_bytes.to_bytes((decrypted_bytes.bit_length() + 7) // 8, 'big')
    return decrypted_message

n = 89951
phi_n = 89352

public_key, private_key = generate_keypair(n, phi_n)

message = input("Enter a message to encrypt: ")

encrypted_message = encrypt(message, public_key)
print("Encrypted message:", encrypted_message)

encrypted_message = "27059"

decrypted_message = decrypt(encrypted_message, private_key)
print("Decrypted message:", decrypted_message)

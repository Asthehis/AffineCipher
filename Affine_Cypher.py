import time

alphabet = {
    'a': '00', 'b': '01', 'c': '02', 'd': '03', 'e': '04', 'f': '05', 'g': '06',
    'h': '07', 'i': '08', 'j': '09', 'k': '10', 'l': '11', 'm': '12', 'n': '13',
    'o': '14', 'p': '15', 'q': '16', 'r': '17', 's': '18', 't': '19', 'u': '20',
    'v': '21', 'w': '22', 'x': '23', 'y': '24', 'z': '25'
}

# Reverse dictionary to map numbers back to letters
reverse_alphabet = {value: key for key, value in alphabet.items()}

def modular_inverse(a, m):
    """Find modular inverse of a under modulo m using Extended Euclidean Algorithm"""
    m0, x0, x1 = m, 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += m0
    return x1

def encrypt_or_decrypt(text: str, k: tuple, mode: str):
    """Generalized function to encrypt or decrypt the text."""
    lower_text = text.lower()
    numeric_values = [alphabet[char] for char in lower_text if char in alphabet]

    if mode == 'encrypt':
        numerical_result = [((int(i)*k[0] + k[1])%26) for i in numeric_values]
    elif mode == 'decrypt':
        k0_inv = modular_inverse(k[0], 26)
        numerical_result = [(((int(i)-k[1]) * k0_inv)%26) for i in numeric_values]
    else:
        raise ValueError("Mode should be either 'encrypt' or 'decrypt'.")

    final_numerical_result = [('0' + str(i)) if i < 10 else str(i) for i in numerical_result]
    result = ''.join([reverse_alphabet[number] for number in final_numerical_result])
    
    return result.upper()

def main():
    print("====== AFFINE CIPHER ======")
    k1 = int(input("Enter the multiplicative cipher key: "))
    k2 = int(input("Enter the additive cipher key: "))
    
    print(f"\n====== PLAINTEXT ======")
    plaintexts = [input(f"Enter the {i+1} plaintext: ") for i in range(10)]  # Collecting 10 plaintext inputs
    
    print(f"\n====== ENCRYPTION ======")
    for p in plaintexts:
        start_time = time.time()
        ciphertext = encrypt_or_decrypt(p, (k1, k2), 'encrypt')
        end_time = time.time()
        encryption_time = end_time - start_time
        print(f"Plaintext: {p}\nCiphertext: {ciphertext}\nEncryption Time: {encryption_time:.6f} seconds")
    
    print(f"\n====== DECRYPTION ======")
    for p in plaintexts:
        ciphertext = encrypt_or_decrypt(p, (k1, k2), 'encrypt')
        start_time = time.time()
        decrypted_text = encrypt_or_decrypt(ciphertext, (k1, k2), 'decrypt')
        end_time = time.time()
        decryption_time = end_time - start_time
        print(f"Ciphertext: {ciphertext}\nDecrypted: {decrypted_text}\nDecryption Time: {decryption_time:.6f} seconds")


if __name__ == "__main__":
    main()

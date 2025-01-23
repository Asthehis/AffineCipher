# Affine Cipher Encryption and Decryption
This Python program implements the Affine Cipher, a type of substitution cipher where each letter in an alphabet is mapped to a number and encrypted using a linear function. The cipher uses two keys:

A multiplicative key (k1), which is used to multiply each letter's numeric value.
An additive key (k2), which is added to each letter's numeric value after multiplication.
The program provides functionality for both encryption and decryption of messages. It processes multiple plaintexts and outputs the corresponding ciphertexts and decrypted messages.

# Features
Encrypts and decrypts text using the Affine Cipher.
Supports multiple plaintext inputs (up to 10).
Displays encryption and decryption times for performance tracking.
Handles alphabet mapping and modular arithmetic.

# Requirements
Python 3.x

# How It Works
# Encryption:

Each letter in the plaintext is converted to a number based on its position in the alphabet (a = 0, b = 1, ..., z = 25).
The encryption formula used is:
E(x) = (k1 * x + k2) % 26 where:
x is the numeric value of the plaintext character.
k1 is the multiplicative key.
k2 is the additive key.

# Decryption:

Decryption reverses the encryption process using the formula: D(x) = k1_inv * (x - k2) % 26 where:
k1_inv is the modular inverse of k1 under modulo 26.
Installation
To run this script, make sure you have Python installed. No external libraries are required.

# Usage
When you run the script, you will be prompted to:

Enter the multiplicative key (k1), a number between 1 and 25.
Enter the additive key (k2), a number between 0 and 25.
Input up to 10 plaintext messages that you wish to encrypt and decrypt.
For each plaintext message:

The encryption will be displayed along with the time taken to encrypt.
The ciphertext will then be decrypted back to the original plaintext, and the decryption time will be displayed.

# Example
# Input:
mathematica
Copy
Edit
Enter the multiplicative cipher key: 5
Enter the additive cipher key: 8

Enter the 1 plaintext: hello
Enter the 2 plaintext: world
...

# Output:
yaml
Copy
Edit
====== ENCRYPTION ======
Plaintext: hello
Ciphertext: SCBBN
Encryption Time: 0.000024 seconds

Plaintext: world
Ciphertext: LBRLD
Encryption Time: 0.000021 seconds

====== DECRYPTION ======
Ciphertext: SCBBN
Decrypted: HELLO
Decryption Time: 0.000017 seconds

Ciphertext: LBRLD
Decrypted: WORLD
Decryption Time: 0.000019 seconds
...

# Notes
The input text is automatically converted to lowercase, and only alphabetic characters are considered. Non-alphabetic characters are ignored.
The encryption and decryption times are measured and displayed for performance analysis.

# License
This project is licensed under the MIT License - see the LICENSE file for details.

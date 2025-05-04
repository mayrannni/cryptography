# 🔐 ECDH Key Exchange with Python
This program shows you a demonstration of the basic operation of **ECDH (Elliptic Curve Diffie-Hellman)** in Python using the `brainpoolP256r1` curve.

## 📈 What is ECDH?
**ECDH** is a cryptographic method for two parties (in this case, Alice and Bob) to generate a shared secret key over an insecure network without "the need" to directly share the key. It's based on ellliptic curve cryptography.

## ✅ What does this script do?
- Generates a private and public key pair for Alice** and Bob.
- Exchanges the public keys.
- Calculates a shared secret key.
- Verifies that both sides derive the same key.
> Note: This example **does not encrypt** the message, it only validates that the key is ready to use. It can be easily extended with AES.

## 🧩 Requirements
Install:
```cmd
pip install tinyec

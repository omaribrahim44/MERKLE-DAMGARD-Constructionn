# 🔐 Merkle–Damgård Hash Construction (SHA-256)

A practical cryptography project that implements the **Merkle–Damgård hash construction** in Python using **SHA-256 as the compression function**, with a focus on **correct padding, verification, and security analysis**.

---

## 📖 Overview

Merkle–Damgård is the foundational design behind widely used hash functions such as **MD5, SHA-1, and SHA-2**.  
This project provides a **clean, modular implementation** of the construction and demonstrates:

- Proper Merkle–Damgård strengthening (padding + length encoding)
- Iterative block-based hashing
- Hash verification against Python’s `hashlib`
- A practical **length extension attack demonstration**

---

## 🎯 Project Goals

- Implement Merkle–Damgård construction correctly from scratch  
- Understand how cryptographic hash functions process arbitrary-length input  
- Validate correctness by comparing with standard SHA-256  
- Demonstrate structural weaknesses such as length extension attacks  

---

## 🧰 Technologies Used

- **Python 3**
- **hashlib (SHA-256)**
- Cryptographic hash function theory

---

## 📁 Project Structure

```text
merkle_damgard/
│── merkle_damgard.py        # Core Merkle–Damgård construction
│── compression.py           # SHA-256 compression function
│── utils.py                 # Padding and helper functions
│── main.py                  # Hash verification and execution
│── length_extension_demo.py # Length extension attack demonstration

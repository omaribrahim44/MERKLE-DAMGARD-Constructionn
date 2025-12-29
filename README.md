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
````

---

## 🛠️ Implementation Details

### 1️⃣ Merkle–Damgård Padding

* Appends `0x80` followed by zero padding
* Appends original message length (64-bit)
* Ensures message length is a multiple of the block size (512 bits)

### 2️⃣ Iterative Block Processing

* Message is divided into fixed-size blocks (64 bytes)
* Each block is processed sequentially using a chaining value

### 3️⃣ Compression Function

* Uses **SHA-256** as the compression function
* Combines the previous chaining value with the current message block

### 4️⃣ Verification

* Final hash output is verified against `hashlib.sha256`
* Ensures correctness and determinism

---

## ▶️ How to Run

### Run hash construction and verification:

```bash
python main.py
```

Example output:

```text
Custom Merkle–Damgard Hash:  785ef210a87b3b703b0a6ce45ce705d4dac0cd3fd75a9257ab0218f8b1700a9e
Standard SHA-256 Hash:      785ef210a87b3b703b0a6ce45ce705d4dac0cd3fd75a9257ab0218f8b1700a9e
✔ Hash verification successful
```

---

## ⚠️ Length Extension Attack Demo

To demonstrate a known weakness of Merkle–Damgård-based hash functions:

```bash
python length_extension_demo.py
```

This shows why **raw hash constructions should not be used for authentication** and highlights the need for secure alternatives such as **HMAC**.

---

## 🔍 Key Concepts Demonstrated

* One-way cryptographic hash functions
* Deterministic hashing
* Collision resistance (theoretical)
* Merkle–Damgård strengthening
* Length extension vulnerability

---

## 📚 Educational Purpose

This project was developed for **academic and learning purposes** to explore cryptographic hash construction principles and security limitations.

---

## 👤 Author

**Omar Ibrahim**


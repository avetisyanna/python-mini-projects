# Hacking The Fender 🖥️🔐

This project is a Python file‑handling exercise focused on working with **CSV**, **TXT**, and **JSON** files.  
It simulates a fictional mission where compromised password data is analyzed, transformed, and rewritten.

> ⚠️ This project is **purely educational** and does **not** involve real hacking or security breaches.

---

## 📌 Project Goals

The mission consists of three main tasks:

1. **Read compromised credentials** from a CSV file  
2. **Extract usernames** and save them into a text file  
3. **Generate new files** to obscure original data and leave a fictional signature

---

## 📂 Files Used

| File Name | Purpose |
|----------|--------|
| `passwords.csv` | Input file containing compromised user data |
| `compromised_users.txt` | Output file listing compromised usernames |
| `boss_message.json` | JSON message confirming mission success |
| `new_passwords.csv` | Overwritten file containing the Slash Null signature |

---

## 🛠️ What the Code Does

### 1. Read CSV Data
- Uses `csv.DictReader`
- Stores each row as a dictionary
- Extracts usernames from the data

### 2. Write Compromised Users
- Saves usernames line‑by‑line into `compromised_users.txt`

### 3. Create a JSON Message
- Writes a structured message to `boss_message.json`
- Uses the `json` module

### 4. Overwrite Password Data
- Replaces password content with a fictional ASCII signature
- Demonstrates writing multi‑line text to a file

---

## 🧪 Technologies Used

- Python 3
- `csv` module
- `json` module
- File I/O (`open`, `read`, `write`)

---

## 🚀 How to Run

1. Make sure `passwords.csv` exists in the same directory
2. Run the script:
   ```bash
   python HackingTheFender.py

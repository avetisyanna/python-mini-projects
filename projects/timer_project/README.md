# ⏳ Station Project 3: Beginner Countdown Timer

A simple, terminal-based countdown timer built in Python. This project was designed to demonstrate core programming logic without relying on external libraries.

## 🚀 Features
- **No Dependencies:** Built using pure Python logic (no `import time`).
- **Error Handling:** Uses `try-except` blocks to prevent crashes if the user enters non-numeric text.
- **Dynamic Display:** Uses carriage returns (`\r`) to update the timer on a single line in the terminal.
- **Time Formatting:** Automatically converts total seconds into a clean `MM:SS` format.

## 🛠️ How it Works
Instead of using a standard sleep function, this script uses a **"Busy-Wait" loop**. It forces the CPU to count to a specific large number to simulate a one-second delay. 
> *Note: Depending on your processor speed, you may need to adjust the counter limit in the code for a more accurate second.*

## 📋 Requirements
- Python 3.x
- No additional libraries or `pip install` required.

## 💻 How to Run
1. Clone this repository to your local machine.
2. Open your terminal or command prompt.
3. Navigate to the project folder.
4. Run the script using:
   ```bash
   python bonus_project.py
   ```

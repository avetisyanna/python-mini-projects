# 🎲 Python Dice Game (Craps)

## 📝 Description
A Python-based simulation of a classic dice game. The program uses logical flow to determine if a player wins, loses, or needs to "roll again" based on the sum of two six-sided dice.

This project demonstrates clean code structure using functions and controlled loops to manage game states.

---

## 🚀 Features
* **Randomized Gameplay:** Uses the Python `random` module to ensure every roll is unique.
* **Game Logic:** * **Instant Win:** Rolling a **7** or **11** on the first try.
    * **Instant Loss:** Rolling a **2**, **3**, or **12** (Casino wins).
    * **The Goal Phase:** If neither happens, the first roll becomes your "goal." You keep rolling until you hit that number again (to win) or roll a **7** (to lose).
* **Automated Loop:** Uses a `while` loop to keep the game running until a final result is reached.

---

## 🛠️ Technical Concepts Used
* **Functions:** `roll_dice()` for modularity and `game_func()` for main logic.
* **Random Module:** Utilizing `random.randint(1, 6)` to simulate real dice.
* **Conditionals:** Complex `if-elif-else` structures to handle different game outcomes.
* **Boolean Flags:** Using `is_on_and_on` to control the `while` loop execution.

---

## 📖 How to Run

### Prerequisites
Make sure you have **Python 3.x** installed.

### Execution
1. **Clone the repository:**
   ```bash
   git clone [https://github.com/avetisyanna/dice_game.git](https://github.com/avetisyanna/dice_game.git)
    ```
2. Navigate to the directory:

```bash
cd dice_game
```
3. Run the script:

```bash
python dice_game.py
```

### 🧠 Key Learnings
Logical Branching: Mapping out a multi-step game process into code.

Infinite Loops: Learning how to safely exit a while True loop using boolean flags.

String Formatting: Using f-strings (f"Rolled a {total}") for clean and readable output.

### Developed as part of the Python programming basics curriculum.
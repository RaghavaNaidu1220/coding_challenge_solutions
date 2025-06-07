# Coding Challenge Solutions

## Introduction
This repository contains solutions to several programming challenges. Each problem is implemented in a separate Python file for better organization and maintainability.

## Folder Structure
```
coding_challenge_solutions/
├── alien_dictionary.py
├── bitwise_matching.py
├── knights_and_portals.py
├── matrix_islands.py
├── mini_interpreter.py
├── sudoku_validator.py
├── README.md
```

## Problem Statements

### 1️⃣ Sudoku Validator With Custom Zones (`sudoku_validator.py`)
- Validate a **9x9 Sudoku board**.
- Ensure **rows, columns**, and **custom zones** (each with 9 unique cells) contain digits `1–9` without repetition.

### 2️⃣ Alien Dictionary (`alien_dictionary.py`)
- Given a sorted list of words from an **alien language**, determine the **character order** used in that language.

### 3️⃣ Knights and Portals (`knights_and_portals.py`)
- Find the **shortest path** in a grid from **top-left to bottom-right**.
- You **may teleport** between any two **empty cells** **exactly once**.

### 4️⃣ Bitwise Matching Pattern (`bitwise_matching.py`)
- Given an integer `n`, return the **next larger integer** that has the same number of `1`s in its **binary representation**.

### 5️⃣ Matrix Islands with Diagonals (`matrix_islands.py`)
- Count the number of **islands** in a matrix of `0`s and `1`s.
- Islands can be formed via **horizontal, vertical**, or **diagonal connections**.

### 🎯 Bonus Challenge: Mini Interpreter (`mini_interpreter.py`)
- Build a simple **interpreter** to:
  - Evaluate `let` variable declarations (e.g., `let x = 5`).
  - Handle basic arithmetic (e.g., `x + 3`, `y * 2`).
  - Parse **if-else conditions** (e.g., `if x > 5 then y = x * 2 else y = x - 2`).

---

## Setup & Running the Code

### 1️⃣ Install Python
Make sure you have Python 3 installed. You can download it from [python.org](https://www.python.org/downloads/).

### 2️⃣ Navigate to the Folder
```bash
cd "D:\Downloads\Telegram Desktop\coding_challenge_solutions"
```

### 3️⃣ Run Each Script
Execute a specific file using:
```bash
python filename.py
```
Example:
```bash
python sudoku_validator.py
```

### 4️⃣ Run All Scripts Sequentially
```bash
python sudoku_validator.py && python alien_dictionary.py && python knights_and_portals.py && python bitwise_matching.py && python matrix_islands.py && python mini_interpreter.py
```

---

## Test Cases Example

### ✅ Sudoku Validator
```python
valid_board = [
    ['5','3','4','6','7','8','9','1','2'],
    ['6','7','2','1','9','5','3','4','8'],
    ['1','9','8','3','4','2','5','6','7'],
    ['8','5','9','7','6','1','4','2','3'],
    ['4','2','6','8','5','3','7','9','1'],
    ['7','1','3','9','2','4','8','5','6'],
    ['9','6','1','5','3','7','2','8','4'],
    ['2','8','7','4','1','9','6','3','5'],
    ['3','4','5','2','8','6','1','7','9']
]

custom_zones = [
    [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)],
    # Add other zones...
]

print("Valid Sudoku:", is_valid_sudoku(valid_board, custom_zones))
```

**Expected Output:**
```
Valid Sudoku: True
```

---

## Future Improvements

- Handle incomplete Sudoku boards (with `.` as empty cells).
- Optimize teleport logic for large grids.
- Extend Mini Interpreter with loops and functions.
- Add GUI support for Sudoku.

---

## Contributors

👨‍💻 Created by **Raghavendra**

Email Id **raghavendrachanda1220@gmail.com**

---











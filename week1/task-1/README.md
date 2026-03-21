```markdown
# Simple Command-Line Calculator

A clean and interactive Python-based calculator that performs basic arithmetic operations. This project demonstrates the use of functional programming,
robust input validation, and Python's modern `match-case` syntax.

# Features
- **Basic Arithmetic:** Supports Addition (+), Subtraction (-), Multiplication (*), and Division (/).
- **Error Handling:** - Prevents crashes during **Division by Zero**.
    - **Input Validation:** Only allows numeric inputs, prompting the user again if they enter text.
- **Continuous Execution:** A `while` loop allows multiple calculations without restarting the script.
- **Utility Commands:** - Type `c` to clear the current session.
    - Type `q` to safely exit the program.
- **Modular Design:** Each operation is isolated in its own function for better readability and maintenance.
---

# Project Structure
```text
Calculator/
├── main.py            # Main application logic
└── README.md          # Documentation
```
---

# How to Run
1. **Ensure Python is installed:** (Python 3.10 or higher is recommended for `match-case` support).
2. **Run the script:**
   ```bash
   python main.py
   ```
---

# Usage Example
```text
--- Simple Command-Line Calculator ---
Operations: +, -, *, /
Type 'c' to clear or 'q' to quit.

Choose an operator (+, -, *, /) or 'q': +
Enter first number: 10
Enter second number: 5

Result: 15.0
```
---

# Technical Logic
- **`try-except` Blocks:** Used in the `getInput` function to catch `ValueError` and ensure the program only processes numbers.
- **`match-case` Statement:** Provides a cleaner and more efficient alternative to multiple `if-elif` statements for operation selection.
- **Infinite Loop with Break:** Manages the user session until the 'q' command is triggered.

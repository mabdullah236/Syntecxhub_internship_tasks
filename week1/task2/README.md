```markdown
# Number Guessing Game

An interactive command-line game where the player tries to guess a randomly generated number. The game features multiple difficulty levels and smart feedback
to guide the user toward the correct answer.

# Features
- **Multiple Difficulty Levels:** - **Easy (e):** Guess between 1-10.
    - **Medium (m):** Guess between 1-50.
    - **Hard (h):** Guess between 1-100.
- **Smart Feedback:** Provides "Choose smaller" or "Choose larger" hints to help the player.
- **Attempt Tracking:** Counts and displays the total number of attempts taken to win.
- **Input Validation:** - Prevents crashes if the user enters text instead of numbers.
    - Ensures guesses stay within the selected level's range.
- **Replayability:** Option to play again or exit after each round.
---

# Project Structure
```text
GuessingGame/
├── main.py            # Main game logic and loops
└── README.md          # Project Documentation
```
---

# How to Run
1. **Clone or Download:** Save the code as `main.py`.
2. **Run the Script:**
   ```bash
   python main.py
   ```
---

# How to Play
1. **Choose a Level:** Select 'e', 'm', or 'h'.
2. **Enter Your Guess:** Input a number based on the range provided.
3. **Follow the Hints:** The game will tell you if your guess is too high or too low.
4. **Win:** Keep guessing until you find the hidden number!
---

# Technical Logic
- **`random.randint()`:** Used to generate a secure random number within the chosen range.
- **Nested Loops:** An outer `while` loop manages the game sessions (replay), and an inner loop handles the guessing process.
- **Error Handling:** Uses `try-except` blocks to catch `ValueError` for non-numeric inputs.
- **Modular Functions:** Separates logic for level selection, random number generation, and input sanitization for cleaner code.

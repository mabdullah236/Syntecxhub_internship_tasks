```markdown
#  Student Management System (CRUD)

A Python-based management system that uses **Object-Oriented Programming (OOP)** principles to manage student records. It allows users to perform
CRUD (Create, Read, Update, Delete) operations with persistent data storage in a JSON file.

# Key Features
- **Persistent Storage:** Saves all student data into a `students.json` file, so records are not lost when the program closes.
- **Data Validation:** - Names are restricted to alphabets only.
    - IDs must be numeric.
    - Grades are strictly limited to valid options (A, B, C, D, F).
- **CRUD Operations:**
    - **Add:** Check for existing IDs to prevent duplicates.
    - **List:** Displays records in a clean, formatted table.
    - **Update:** Modify existing names or grades without changing the ID.
    - **Delete:** Remove students by their unique ID.
- **OOP Architecture:** Uses `Student` and `StudentManager` classes for better code organization.
---

# Project Structure
```text
StudentManagement/
├── main.py            # Main application logic and menu loop
├── students.json      # JSON file where data is stored (Auto-generated)
└── README.md          # Documentation
```
---

# How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/student-management-system.git](https://github.com/your-username/student-management-system.git)
   cd student-management-system
   ```
2. **Run the script:**
   No external libraries are required as it uses Python's built-in `json` module.
   ```bash
   python main.py
   ```
---

# Usage Example
Upon running the script, you will see a menu:
1. **Add Student:** Input Name, ID, and Grade. The system validates the input before saving.
2. **List Students:** Shows all records in a tabular format.
3. **Delete Student:** Enter the ID to remove a specific student.
4. **Update Student:** Enter ID to change the Name or Grade.
5. **Exit:** Safely closes the program.
---

# Technical Logic
- **`json.dump()` & `json.load()`:** Used to convert Python objects to JSON and vice versa.
- **List Comprehension:** Used in `delete_student` and `load_data` for concise and efficient data filtering.
- **Exception Handling:** Includes `try-except` blocks to handle missing `students.json` files gracefully.
```

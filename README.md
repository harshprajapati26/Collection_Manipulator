# 📚 Collection Manipulator

## 📌 Project Overview

**Collection Manipulator** is a Python console-based program called **Student Data Organizer** that manages and manipulates a collection of student records.

The project demonstrates important Python concepts such as:

- String formatting
- Lists
- Tuples
- Sets
- Dictionaries
- Mutability and immutability
- Type casting
- `del` keyword
- Menu-driven programming
- User input and data manipulation

---

## 🎯 Objective

The main objective of this project is to create a simple **Student Data Organizer** that allows users to:

- Add student records
- Display all students
- Update student information
- Delete student records
- Display unique subjects offered by students

The program stores and organizes student information using different Python collection data types.

---

## ✨ Features

### 👨‍🎓 Add Student
Allows the user to enter:

- Student ID
- Student Name
- Age
- Grade
- Date of Birth
- Subjects

Student information is then stored using appropriate Python collection types.

### 📋 Display All Students
Displays all stored student records in a user-friendly formatted output.

Example:

```text
Student ID: 101 | Name: Harsh | Age: 20 | Grade: A+
Subjects: Math, Science, English
```

### ✏️ Update Student
Allows the user to update specific information such as:

- Age
- Grade
- Subjects

using the student's ID.

### 🗑️ Delete Student
Removes a student record from the main list using the `del` keyword.

### 📚 Display Subjects Offered
Displays all unique subjects available among students using a **Set**, which automatically prevents duplicate subjects.

---

## 🧠 Python Concepts Used

| Concept | Usage |
|--------|-------|
| **List** | Stores multiple student records |
| **Tuple** | Stores fixed information such as Student ID and Date of Birth |
| **Set** | Stores unique subjects |
| **Dictionary** | Stores student details using Student ID as the key |
| **String Formatting** | Displays information in a readable format |
| **Type Casting** | Converts user input into required data types |
| **Mutability** | Demonstrates modification of list/dictionary data |
| **Immutability** | Demonstrates fixed tuple data |
| **`del` Keyword** | Deletes student records |
| **Loops** | Handles repeated menu operations |
| **Conditional Statements** | Handles menu choices and validations |

---

## 🗂️ Data Structure

### List

Used to store multiple student records.

```python
students = []
```

### Tuple

Used for information that should not change.

```python
student_id_dob = (101, "2002-05-14")
```

### Set

Used to store unique subjects.

```python
subjects = {"Math", "Science", "English"}
```

### Dictionary

Used to organize student information.

```python
student = {
    "name": "Harsh",
    "age": 20,
    "grade": "A+",
    "subjects": ["Math", "Science", "English"]
}
```

---

## 🔄 Program Flow

```text
Start
  │
  ▼
Welcome Message
  │
  ▼
Display Menu
  │
  ├── 1. Add Student
  │
  ├── 2. Display All Students
  │
  ├── 3. Update Student
  │
  ├── 4. Delete Student
  │
  ├── 5. Display Subjects Offered
  │
  └── 6. Exit
          │
          ▼
        End
```

---

## 💻 Menu Options

```text
Select an option:

1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects Offered
6. Exit
```

---

## ▶️ Example Console Output

```text
Welcome to the Student Data Organizer!

Select an option:
1. Add Student
2. Display All Students
3. Update Student
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice: 1

Enter student details:
Student ID: 101
Name: Harsh
Age: 20
Grade: A+
Date of Birth : 2002-05-14
Subjects (comma-separated): Math, Science, English

Student added successfully!
```

### Display Students

```text
Display All Students

Student ID: 101 | Name: Harsh | Age: 20 | Grade: A+
Subjects: Math, Science, English
```

---

## 📂 Project Structure

```text
Collection-Manipulator/
│
├── collection_manipulator.py
│
├── README.md
│
└── demo/
    └── program-demo.mp4
```

---

## ⚙️ Requirements

To run this project, you need:

- Python 3.x
- Any Python IDE or code editor
- Command Prompt / Terminal

No external libraries are required.

---

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

### 2. Open the Project Folder

```bash
cd Collection-Manipulator
```

### 3. Run the Python Program

```bash
python collection_manipulator.py
```

---

## 🎥 Project Video

Watch the complete demonstration of the **Collection Manipulator / Student Data Organizer** here:

### 🔗 Video Link

**[▶️ Watch Project Demo](PASTE_YOUR_VIDEO_LINK_HERE)**

> 📌 Replace `PASTE_YOUR_VIDEO_LINK_HERE` with your YouTube, Google Drive, or other video link.

---

## 🎓 Learning Outcomes

After completing this project, you will understand how to:

- Work with Python collections
- Store and organize structured data
- Use Lists, Tuples, Sets, and Dictionaries
- Handle user input
- Perform type casting
- Modify mutable collections
- Work with immutable tuples
- Remove data using `del`
- Create menu-driven Python applications
- Format output for better readability

---

## 👨‍💻 Author

HARSH PRAJAPATI

### Language

🐍 **Python 3**

---

## ⭐ Conclusion

The **Collection Manipulator** project is a simple and practical Python application designed to demonstrate the use of different collection data types while managing student records.

It provides hands-on practice with **Lists, Tuples, Sets, Dictionaries, string formatting, mutability, immutability, type casting, and the `del` keyword**.

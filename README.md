# Library Management System

**A terminal-based Python mini project for managing library books.**

This project helps a librarian add books, view records, search books, issue books, return books, and delete book details. It uses a simple menu-driven interface and stores all book data in a JSON file.

## Synopsis

The Library Management System helps a user add, view, search, issue, return, and delete books. Book records are saved in a JSON file, so the data remains available after closing the program.

## Features

- Add new books
- View all books in a neat table
- Search books by title or author
- Issue books and reduce available copies
- Return books and increase available copies
- Delete book records
- Save and load book data using `books.json`
- Simple validation for wrong input and unavailable books

## Concepts Used

- Python classes and objects
- File handling
- JSON storage
- Lists and dictionaries
- Loops and conditionals
- Functions
- Input validation

## Project Files

- `main.py` - Main Python program
- `books.json` - Stores book records
- `README.md` - Project documentation

## How To Run

1. Install Python on your computer.
2. Open terminal or command prompt in this project folder.
3. Run the program:

```bash
python main.py
```

If your system uses `python3`, run:

```bash
python3 main.py
```

## Sample Output

```text
Library Management System
1. Add Book
2. View All Books
3. Search Book
4. Issue Book
5. Return Book
6. Delete Book
7. Exit
Enter your choice (1-7): 2

All Books
----------------------------------------------------------------------------------
ID      Title                     Author                Total     Available
----------------------------------------------------------------------------------
B001    Python Basics             John Smith            3         3
B002    Data Structures           Anita Sharma          2         2
B003    Clean Code                Robert Martin         1         1
----------------------------------------------------------------------------------
```

## Future Improvements

- Add student/member records
- Store issue dates and return dates
- Add fine calculation for late returns
- Add login for librarian/admin

## Author

Created as a Python mini project for Anudip Foundation.

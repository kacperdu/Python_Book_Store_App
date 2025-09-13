# Python_Book_Store_App
An interactive Python BookStore Management System built in PyCharm. Features separate user and admin roles.
App allows customers to borrow and return books, while admins can manage the inventory.
Persistent data is stored in text files, and the project demonstrates file handling, validation and version control with Git

Features:
  - Interactive Menu:
    - User-friendly navigation for borrowing, returning, and reviewing books.

  - User Role:
      - Borrow up to 4 books at a time.
      - Input validation for names (1–20 characters) and membership numbers (6-digit numeric).
      - Review borrowed books and due dates (7 days from borrowing).
      - Return borrowed books, updating the system automatically.

- Admin Role:
    - Add new books to inventory.  
    - Remove books from the system.  
    - Update available copies or borrowed counts.  
    - View the full inventory.

- Persistent Data Storage:
  - Inventory stored in `book_inventory.txt`.  
  - Borrowed books tracked in `Borrowed_Books.txt`.  
  - Backup inventory included (`invas.txt`).  

Tech Stack:
  - Language: Python 3
  - IDE: PyCharm
  - Data Storage: Text files .txt
  - Version Control: Git + GitHub

Author:
Kacper Duda

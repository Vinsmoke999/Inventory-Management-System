Inventory Management System

(Python)

📌 Overview

This project is a simple command-line based Inventory Management System written in Python. It helps store, update, and manage items (called Saman) with their details such as ID, Name, Price, and Quantity.

The program uses a text file (Saman.txt) to save and load data, ensuring that the inventory remains available even after the program is closed.


---

🛠 Features

1. View All Saman

Displays a list of all stored items along with their ID, name, price, and quantity.

2. Add New Saman

Allows the user to add a new item after verifying that the ID is unique.

3. Update Stock

Enables the user to either add stock or sell stock, updating the quantity accordingly.

4. Auto Save & Load

Data is automatically loaded from Saman.txt when the program starts.

All changes are saved back to the file.


5. Exit Option

Clean exit from the inventory system.


---

📁 File Details

Saman.txt (Data File)

Each line stores item details as:

ID,Name,Price,Quantity

Example:

101,Pen,10.0,50
102,Notebook,50.0,20


---

🧩 How the Code Works

1. load_data()

Loads existing inventory from Saman.txt into a global list.

2. save_to_file()

Saves the current list of items back to the file.

3. add_Saman()

Prompts the user for item details and adds it to inventory.

4. show_Saman_items()

Displays all items in a structured format.

5. update_stock()

Searches for an item by ID and updates its quantity.

6. Infinite Menu Loop

Runs until the user selects option 4 (Exit).


---

▶ Running the Program

1. Save the Python code in a file (e.g., inventory.py).


2. Ensure that Saman.txt is in the same directory (it will be created automatically if missing).


3. Run the script:



python inventory.py

4. Follow the on-screen menu.




---

📌 Notes

Input validation is minimal; ensure valid numeric inputs for price and quantity.

The file-based storage makes the system simple but not ideal for large datasets.

This is a beginner‑friendly inventory project suitable for assignments or practice.



---

✔ Conclusion

This Inventory Management System provides a simple yet functional way to manage items using Python. It can be enhanced further with features like search, delete, sorting, or using JSON/SQLite for better data handling.


---

Thank you for using the Inventory Management System!

# CRUD-Toko-Jam
Built with Python, the app follows the CRUD operation (Create, Read, Update, Delete)


# Business Understanding
This program was developed as a simple and practical solution to help manage the sales and inventory of luxury watches. Designed for use in small to medium-sized watch stores, the system provides essential features. The dummy data is based on a fictional company named "Toko Jam Wild'

# Features 
1. Create
    - Adding new watch data.
    - Prevent duplicate data ( same name with different year of pruduction is allowed )

2. Read
    - Displaying all watches data.
    - Displaying all wacthes based on columns (code or name or year of production, etc)

3. Update
    - Modifying watch data.
    - Prevent duplicate updates.

4. Delete
    - Delete watch data based on selected code.

5. Additional Features
    - Printing purchase receipts.

# How To Acces
1. Download the file

3. Check your Python version, make sure its 3.7 or latest version

3. Install the tabulate Python library
```python
pip install tabulate
```

4. Run the program

  

# Flow
1. Program Start and Main Menu Display
    Upon launching the program, the system presents the user with a main menu containing several options. These options allow users to interact with the watch inventory data,          either   for administrative tasks or purchase activities.

2. Inventory Data Structure
   All watch data is stored in a list of dictionaries. Each dictionary represents one watch and contains the following attributes:

  kode: Unique identifier
  nama: Name of the watch
  kategori: Watch category (e.g., male,female,unisex)
  stok: Available quantity
  harga: Price per unit
  tahun: Year of production
  This structure allows efficient lookup, modification, and management of records.

3. Functional Flow Options
  - View Watch List
    Displays all watches in a table format using the tabulate library.
    Useful for both admins and customers to see available products.
  - Add New Watch (Admin)
    Admin inputs a new watch’s details.
    System validates the input.
    The watch is appended to the inventory list.
 - Update Watch Data (Admin)
    Admin selects a watch by its code.
    The system displays current data.
    Admin provides new values for selected fields.
    The dictionary in the list is updated accordingly.
  - Delete Watch (Admin)
    Admin selects a watch to delete.
    The system confirms deletion.
    The dictionary is removed from the list.
  - Purchase Watch (Customer)
    Customer selects a watch and inputs desired quantity.
    System checks availability.
    If valid, stock is reduced and total cost is calculated.
    System generates a purchase receipt and displays transaction details.
  - Search Watch
    Allows searching by name or category.
    Matches are filtered and displayed to the user.
 - Print Receipt
    Displays transaction summary (watch name, quantity, total price).
    Helps simulate real transaction flow.
   - Exit

    Ends the program session.



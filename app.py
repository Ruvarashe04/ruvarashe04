import tkinter as tk
from tkinter import ttk
import psycopg2

# Create a connection to the PostgreSQL database
db = psycopg2.connect(
    host="localhost",
    database="TapsCurry",
    user="postgres",
    password="1902"
)
cursor = db.cursor()


def add_record():
    name = name_entry.get()
    age = int(age_entry.get())
    email = email_entry.get()
    date_of_birth = dob_entry.get()

    # Insert the record into the database
    cursor.execute(
        "INSERT INTO records (\"Name\", \"Age\", \"Email\", \"DateOfBirth\") VALUES (%s, %s, %s, %s)",
        (name, age, email, date_of_birth)
    )
    db.commit()

    status_label.config(text="Record added successfully!")


def sort_records():
    sort_field = sort_field_combobox.get()
    sort_order = sort_order_combobox.get()

    # Fetch records from the database and sort them
    cursor.execute(f"SELECT * FROM records ORDER BY \"{sort_field}\" {sort_order}")
    records = cursor.fetchall()

    display_records(records)


def search_records():
    search_term = search_entry.get()
    search_algorithm = search_algorithm_combobox.get()

    # Perform search using the selected algorithm
    if search_algorithm == 'exact_match':
        cursor.execute(f"SELECT * FROM records WHERE \"Name\" = '{search_term}'")
    elif search_algorithm == 'partial_match':
        cursor.execute(f"SELECT * FROM records WHERE \"Name\" LIKE '%{search_term}%'")

    records = cursor.fetchall()

    display_records(records)


def display_records(records):
    # Clear the current table contents
    for row in result_treeview.get_children():
        result_treeview.delete(row)

    # Insert the fetched records into the table
    for record in records:
        result_treeview.insert("", tk.END, values=record)


# Create the main application window
root = tk.Tk()
root.title("Record Management")

# Create the record form
form_frame = ttk.LabelFrame(root, text="Add New Record")
form_frame.pack(padx=10, pady=10)

name_label = ttk.Label(form_frame, text="Name:")
name_label.grid(row=0, column=0, sticky=tk.W)
name_entry = ttk.Entry(form_frame)
name_entry.grid(row=0, column=1)

age_label = ttk.Label(form_frame, text="Age:")
age_label.grid(row=1, column=0, sticky=tk.W)
age_entry = ttk.Entry(form_frame)
age_entry.grid(row=1, column=1)

email_label = ttk.Label(form_frame, text="Email:")
email_label.grid(row=2, column=0, sticky=tk.W)
email_entry = ttk.Entry(form_frame)
email_entry.grid(row=2, column=1)

dob_label = ttk.Label(form_frame, text="Date Of Birth:")
dob_label.grid(row=3, column=0, sticky=tk.W)
dob_entry = ttk.Entry(form_frame)
dob_entry.grid(row=3, column=1)

add_button = ttk.Button(form_frame, text="Add Record", command=add_record)
add_button.grid(row=4, columnspan=2)

status_label = ttk.Label(root, text="")
status_label.pack()

# Create the sorting interface
sort_frame = ttk.LabelFrame(root, text="Sorting")
sort_frame.pack(padx=10, pady=10)

sort_field_label = ttk.Label(sort_frame, text="Choose Column to Sort By:")
sort_field_label.grid(row=0, column=0, sticky=tk.W)
sort_field_combobox = ttk.Combobox(sort_frame, values=["Name", "Age", "Email", "DateOfBirth"])
sort_field_combobox.grid(row=0, column=1)
sort_field_combobox.current(0)

sort_order_label = ttk.Label(sort_frame, text="Sort Order:")
sort_order_label.grid(row=1, column=0,sticky=tk.W)
sort_order_combobox = ttk.Combobox(sort_frame, values=["ASC", "DESC"])
sort_order_combobox.grid(row=1, column=1)
sort_order_combobox.current(0)

sort_button = ttk.Button(sort_frame, text="Sort", command=sort_records)
sort_button.grid(row=2, columnspan=2)

# Create the search interface
search_frame = ttk.LabelFrame(root, text="Searching")
search_frame.pack(padx=10, pady=10)

search_entry = ttk.Entry(search_frame)
search_entry.grid(row=0, column=0)

search_algorithm_combobox = ttk.Combobox(search_frame, values=["exact_match", "partial_match"])
search_algorithm_combobox.grid(row=0, column=1)
search_algorithm_combobox.current(0)

search_button = ttk.Button(search_frame, text="Search", command=search_records)
search_button.grid(row=1, columnspan=2)

# Create the result table
result_treeview = ttk.Treeview(root, columns=("name", "age", "email", "date_of_birth"), show="headings")
result_treeview.pack(padx=10, pady=10)

result_treeview.heading("name", text="Name")
result_treeview.heading("age", text="Age")
result_treeview.heading("email", text="Email")
result_treeview.heading("date_of_birth", text="Date Of Birth")

# Start the application
root.mainloop()
import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


#host='localhost',username='root',password='sonu296702@gmail',database='management'

# Connect to the database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="sonu296702@gmail",
    database="management"
)

# Retrieve data from the database
cursor = db.cursor()
cursor.execute("SELECT * FROM criminal")
data = cursor.fetchall()

# Create a tkinter window
root = tk.Tk()
root.title("Report")

# Create a table to display the data
table = ttk.Treeview(root)
table["columns"] = ["Case_id", "Criminal_no", "Criminal_name","arrest_date","dateOfcrime","age","crimeType"]
table.heading("Case_id", text="Case_id")
table.heading("Criminal_no", text="Criminal_no")
table.heading("Criminal_name", text="Criminal_name")
table.heading("arrest_date", text="arrest_date")
table.heading("dateOfcrime", text="dateOfcrime")
table.heading("age", text="age")
table.heading("crimeType", text="crimeType")
table.heading("Criminal_name", text="Criminal_name")

for row in data:
    table.insert("", tk.END, values=row)

# Pack the table
table.pack()

# Create a button to export the data
def export_data():
    filename = filedialog.asksaveasfilename(defaultextension=".xlsx")
    if filename:
        with open(filename, "w") as f:
            # Write the column headers
            f.write("Case_id,Criminal_no, Criminal_name,arrest_date,dateOfcrime,age,crimeType\n")
            # Write the data rows
            for row in data:
                f.write(",".join(str(x) for x in row) + "\n")

export_button = tk.Button(root, text="Export", command=export_data)
export_button.pack()

# Start the tkinter event loop
root.mainloop()

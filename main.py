import tkinter as tk
from tkinter import messagebox

def validate_date(entry):
    # Validate the date format (DD/MM/YYYY)
    date_str = entry.get()
    if not date_str.isdigit() or len(date_str) != 8:
        messagebox.showerror("Error", "Invalid date format. Please enter DDMMYYYY.")
        entry.delete(0, tk.END)

def submit_tutor_web():
    # Function to handle the submission of the tutor web form
    # You can add your logic here to process the input data
    day_start = entry_day_start.get()
    month_start = entry_month_start.get()
    year_start = entry_year_start.get()
    
    day_end = entry_day_end.get()
    month_end = entry_month_end.get()
    year_end = entry_year_end.get()

    start_date = f"{day_start}/{month_start}/{year_start}"
    end_date = f"{day_end}/{month_end}/{year_end}"

    print(f"Start Date: {start_date}")
    print(f"End Date: {end_date}")
    print("Tutor web submitted!")

# Create the main window
root = tk.Tk()
root.title("Tutor web")

# Validation function to allow only numeric input
validate_cmd = (root.register(lambda char: char.isdigit()), "%S")

# Create and pack labels and entry widgets for start date
label_start = tk.Label(root, text="Start Date (DDMMYYYY):")
label_start.grid(row=0, column=0, padx=10, pady=5, sticky="e")

entry_day_start = tk.Entry(root, width=5, validate="key", validatecommand=validate_cmd)
entry_day_start.grid(row=0, column=1, pady=5)
entry_day_start.insert(0, "DD")

entry_month_start = tk.Entry(root, width=5, validate="key", validatecommand=validate_cmd)
entry_month_start.grid(row=0, column=2, pady=5)
entry_month_start.insert(0, "MM")

entry_year_start = tk.Entry(root, width=8, validate="key", validatecommand=validate_cmd)
entry_year_start.grid(row=0, column=3, pady=5)
entry_year_start.insert(0, "YYYY")

# Create and pack labels and entry widgets for end date
label_end = tk.Label(root, text="End Date (DDMMYYYY):")
label_end.grid(row=1, column=0, padx=10, pady=5, sticky="e")

entry_day_end = tk.Entry(root, width=5, validate="key", validatecommand=validate_cmd)
entry_day_end.grid(row=1, column=1, pady=5)
entry_day_end.insert(0, "DD")

entry_month_end = tk.Entry(root, width=5, validate="key", validatecommand=validate_cmd)
entry_month_end.grid(row=1, column=2, pady=5)
entry_month_end.insert(0, "MM")

entry_year_end = tk.Entry(root, width=8, validate="key", validatecommand=validate_cmd)
entry_year_end.grid(row=1, column=3, pady=5)
entry_year_end.insert(0, "YYYY")

# Create and pack a submit button
submit_button = tk.Button(root, text="Start", command=submit_tutor_web)
submit_button.grid(row=2, columnspan=4, pady=20)

# Start the Tkinter event loop
root.mainloop()

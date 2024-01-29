import tkinter as tk
from tkinter import messagebox
from Turo_Crawler import call_Tutor

def validate_date(entry):
    # Validate the date format (DD/MM/YYYY)
    date_str = entry.get()
    if not date_str.isdigit() or len(date_str) != 8:
        messagebox.showerror("Error", "Invalid date format. Please enter DDMMYYYY.")
        entry.delete(0, tk.END)

def format_two_digits(input_number):
    # Convert the input to an integer
    input_number = int(input_number)
    
    # Ensure the number is within the range [0, 99]
    formatted_number = max(0, min(input_number, 99))
    
    # Convert the formatted number back to a string and add leading zeros if necessary
    return f"{formatted_number:02d}"

def submit_tutor_web():
    # Function to handle the submission of the tutor web form
    # You can add your logic here to process the input data
    Day_Start = format_two_digits(entry_day_start.get())
    Month_Start = format_two_digits(entry_month_start.get())
    Year_Start = entry_year_start.get()
    
    Day_End = format_two_digits(entry_day_end.get())
    Month_End = format_two_digits(entry_month_end.get())
    Year_End = entry_year_end.get()

    print("Tutor web submitted!")
    ###MAIN CODE####
    month_dict = {'01':'Jan', '02':'Feb', '03':'Mar', '04':'Apr', '05':'May', '06':'Jun','07':'Jul', '08':'Aug', '09':'Sep', '10':'Oct', '11':'Nov', '12':'Dec'}

    # Day_Start = '01'
    # Month_Start = '02'
    # Year_Start = '2024'
    Start = 'startDate=' +str(Month_Start) + '%2F' + str(Day_Start) +   '%2F' + str(Year_Start)  ###  month%2F   day%2F    year
    Savetime_start = month_dict.get(Month_Start) + Day_Start + Year_Start

    # Day_End= '08'
    # Month_End = '02'
    # Year_End = '2024'
    End = 'endDate=' +str(Month_End) + '%2F' + str(Day_End)+   '%2F' + str(Year_End)   ###  month%2F   day%2F    year
    Savetime_end = month_dict.get(Month_End) + Day_End + Year_End

    Savetime = '_' + Savetime_start + '_' + Savetime_end

    part1 = 'https://turo.com/us/en/search?country=US&defaultZoomLevel=13&deliveryLocationType=city&'
    part2 = '&endTime=12%3A00&isMapSearch=false&itemsPerPage=200&latitude=33.6832497&location=Irvine%2C%20CA%2092614%2C%20USA&locationType=CITY&longitude=-117.83407349999999&pickupType=ALL&placeId=ChIJGWp61inc3IARB84fEAnUP0U&region=CA&sortType=RELEVANCE&'
    part3 = '&startTime=11%3A00&useDefaultMaximumDistance=true'

    url = str(part1) + End + part2 + Start + part3
    print(url)
    print(call_Tutor(url,Savetime))
    

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

label_example = tk.Label(root, text="Example: DDMMYYY = 01082024")
label_example.grid(row=2, column=0, padx=10, pady=5, sticky="e")

# Create and pack a submit button
submit_button = tk.Button(root, text="Start", command=submit_tutor_web)
submit_button.grid(row=3, columnspan=4, pady=20)

# Start the Tkinter event loop
root.mainloop()

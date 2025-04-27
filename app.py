import tkinter as tk
from tkinter import ttk

def length_convetor(value, from_unit, to_unit):
    # Conversion factors for the units
    conversion_factor = {
        "meter": 1,
        "kilometer": 0.001,  # Correct factor: 1 meter = 0.001 kilometers
        "inches": 39.3701,
        "feet": 3.28084
    }

    # If either from_unit or to_unit is invalid
    if from_unit not in conversion_factor or to_unit not in conversion_factor:
        return "Invalid unit selected"

    # Correct formula for conversion
    return value * conversion_factor[to_unit] / conversion_factor[from_unit]

def convert_unit():
    try:
        value = float(entry_value.get())  # Get value from the entry box
        from_unit = combo_from.get()      # Get the "from" unit
        to_unit = combo_to.get()          # Get the "to" unit
        category = combo_category.get()   # Get the category

        # Perform conversion only if the category is "length"
        if category == "length":
            result = length_convetor(value, from_unit, to_unit)
            label_result.config(text=f"Result: {result:.2f} {to_unit}")  # Display result
        else:
            label_result.config(text="Unsupported category")  # Error if category is not length

    except ValueError:
        label_result.config(text="Please enter a valid number")  # Error for invalid input

# Main application window
root = tk.Tk()
root.title("Unit Converter")
root.geometry("500x400")

# Dropdown for category
label_category = tk.Label(root, text="Select category:")
label_category.pack(pady=5)
combo_category = ttk.Combobox(root, values=["length"], state="readonly")
combo_category.current(0)  # Default to "length"
combo_category.pack(pady=5)

# Dropdown for "from" units
label_from = tk.Label(root, text="Convert from:")
label_from.pack(pady=5)
combo_from = ttk.Combobox(root, values=["meter", "kilometer", "inches", "feet"], state="readonly")
combo_from.current(0)  # Default to "meter"
combo_from.pack(pady=5)

# Dropdown for "to" units
label_to = tk.Label(root, text="Convert to:")
label_to.pack(pady=5)
combo_to = ttk.Combobox(root, values=["meter", "kilometer", "inches", "feet"], state="readonly")
combo_to.current(1)  # Default to "kilometer"
combo_to.pack(pady=5)

# Entry for value input
label_value = tk.Label(root, text="Enter value:")
label_value.pack(pady=5)
entry_value = tk.Entry(root)
entry_value.pack(pady=5)

# Button to perform conversion
button_convert = tk.Button(root, text="Convert", command=convert_unit)
button_convert.pack(pady=11)

# Label to display result
label_result = tk.Label(root, text="Result:", font=("Arial", 15))
label_result.pack(pady=22)

# Run the application
root.mainloop()

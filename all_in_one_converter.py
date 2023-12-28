from tkinter import *
import tkinter as tk
# defining the reset function
def reset():
    input_field.delete(0, END)
    output_field.delete(0, END)
    input_value.set(SELECTIONS[0])
    output_value.set(SELECTIONS[0])
    input_field.focus_set()
# defining the convert function
def convert():
    input_unit = input_value.get()
    output_unit = output_value.get()
# using if statement if the type of units are no the same
    if input_unit != output_unit:
        input_amount = float(input_field.get())
        conversion_factor = unit_dict[input_unit] / unit_dict[output_unit]
        output_amount = input_amount * conversion_factor
        output_field.delete(0, END)
        output_field.insert(0, str(output_amount))

# defining the values of the units
unit_dict = {
    "millimeter": 0.001,
    "centimeter": 0.01,
    "meter": 1.0,
    "kilometer": 1000.0,
    "foot": 0.3048,
    "mile": 1609.344,
    "yard": 0.9144,
    "inch": 0.0254,
    "square meter": 1.0,
    "square kilometer": 1000000.0,
    "square centimeter": 0.0001,
    "square millimeter": 0.000001,
    "are": 100.0,
    "hectare": 10000.0,
    "acre": 4046.856,
    "square mile": 2590000.0,
    "square foot": 0.0929,
    "cubic meter": 1000.0,
    "cubic centimeter": 0.001,
    "litre": 1.0,
    "millilitre": 0.001,
    "gallon": 3.785,
    "gram": 1.0,
    "kilogram": 1000.0,
    "milligram": 0.001,
    "quintal": 100000.0,
    "ton": 1000000.0,
    "pound": 453.592,
    "ounce": 28.3495
}
# specfying which units are which for type
length_units = ["millimeter", "centimeter", "meter", "kilometer", "foot", "mile", "yard", "inch"]
temperature_units = ["celsius", "fahrenheit"]
area_units = ["square meter", "square kilometer", "square centimeter", "square millimeter",
              "are", "hectare", "acre", "square mile", "square foot"]
volume_units = ["cubic meter", "cubic centimeter", "litre", "millilitre", "gallon"]
weight_units = ["gram", "kilogram", "milligram", "quintal", "ton", "pound", "ounce"]

SELECTIONS = ["Select Unit"] + length_units + temperature_units + area_units + volume_units + weight_units

# Create the main GUI window
window = tk.Tk()
window.title("All in one converter")
window.geometry("500x500+500+250")
window.resizable(1, 1)
window.configure(bg="#e0f2f1")  

header_frame = Frame(window, bg="#e0f2f1")  
body_frame = Frame(window, bg="#e0f2f1")

header_label = Label(header_frame, text="All in one converter", font=("arial black", 18), bg="#16a085", fg="#e8f6f3")

# Create input and output unit selection variables
input_value = StringVar(window)
output_value = StringVar(window)

# Set default values for unit selection
input_value.set(SELECTIONS[0])
output_value.set(SELECTIONS[0])

# Create input and output unit selection menus
input_unit_menu = OptionMenu(body_frame, input_value, *SELECTIONS)
output_unit_menu = OptionMenu(body_frame, output_value, *SELECTIONS)

# Create input and output entry fields
input_field = Entry(body_frame, font=("arial", 14))
output_field = Entry(body_frame, font=("arial", 14))

# Create Convert and Reset buttons
convert_button = Button(body_frame, text="Convert", command=convert)
reset_button = Button(body_frame, text="Reset", command=reset, bg="red", fg="white")  # Change the reset button color to red

# Layout the widgets using the grid layout manager
input_unit_menu.grid(row=0, column=0, padx=10, pady=10)
input_field.grid(row=0, column=1, padx=10, pady=10)
output_unit_menu.grid(row=1, column=0, padx=10, pady=10)
output_field.grid(row=1, column=1, padx=10, pady=10)
convert_button.grid(row=2, column=0, columnspan=2, pady=10)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)

header_frame.pack(fill="x")
header_label.pack(pady=10)
body_frame.pack(expand=True, fill="both")

# Run the Tkinter event loop
window.mainloop()

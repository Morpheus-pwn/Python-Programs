# Write a GUI program to inputs the integer, computes the square root, and outputs the result and handles input errors by displaying a message box.

import tkinter as tk
import tkinter.messagebox as messagebox
import math

def calculate_sqrt():
    try:
        number = int(input_entry.get())
        sqrt = math.sqrt(number)
        output_label.config(text=f"Square root: {sqrt:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer.")

window = tk.Tk()
window.title("Square Root Calculator")

input_label = tk.Label(window, text="Enter an integer:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

calculate_button = tk.Button(window, text="Calculate Square Root", command=calculate_sqrt)
calculate_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
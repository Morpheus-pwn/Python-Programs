# Write GUI program to compute and displays the square root of an input number.

import tkinter as tk
from tkinter import ttk

def calculate_sqrt():
  try:
    num = float(entry.get())
    if num >= 0:
      sqrt_result = num ** 0.5
      result_label.config(text=f"Square root of {num} is: {sqrt_result:.2f}")
    else:
      result_label.config(text="Please enter a non-negative number.")
  except ValueError:
    result_label.config(text="Invalid input. Please enter a number.")

window = tk.Tk()
window.title("Square Root Calculator")

input_label = ttk.Label(window, text="Enter a number:")
input_label.pack()
entry = ttk.Entry(window)
entry.pack()

calculate_button = ttk.Button(window, text="Calculate", command=calculate_sqrt)
calculate_button.pack()

result_label = ttk.Label(window, text="")
result_label.pack()

window.mainloop()

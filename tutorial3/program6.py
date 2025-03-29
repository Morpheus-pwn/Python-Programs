# Write a GUI program to convert an input string to uppercase and displays the result.

import tkinter as tk

def convert_to_uppercase():
    input_text = input_entry.get()
    uppercase_text = input_text.upper()
    output_label.config(text=uppercase_text)

window=tk.Tk()
window.title("string to uppercase")

input_label=tk.Label(window,text="Enter a string:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

convert_button = tk.Button(window, text="Convert to Uppercase", command=convert_to_uppercase)
convert_button.pack()

output_label = tk.Label(window, text="")
output_label.pack()

window.mainloop()
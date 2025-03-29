# Write a GUI based program that allows the user to convert temperature values between degrees Fahrenheit and degrees Celsius.  The interface should have labeled entry fields for these two values. These components should arrange in a grid where the labels occupy the first row and the corresponding field occupy the second row. At start up the Fahrenheit field should contain 32 and the Celsius field contain 0.0.The third row in the window contain two command buttons ,labeled >>>> and <<<<.When the user presses the first button, the program should use the data in the Fahrenheit field to compute the Celsius value, which should then be output to the Celsius field. The second button should perform the inverse function.

from tkinter import *
from tkinter import ttk
import math

class ConvertTemp(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Temperature Converter")
        self.grid()
        self.createWidgets()

    def createWidgets(self):
        self.f_label = Label(self, text="Fahrenheit")
        self.f_label.grid(row=0, column=0)
        self.f_entry = Entry(self)
        self.f_entry.grid(row=1, column=0)
        self.c_label = Label(self, text="Celsius")
        self.c_label.grid(row=0, column=1)
        self.c_entry = Entry(self)
        self.c_entry.grid(row=1, column=1)
        self.f_to_c = Button(self, text=">>", command=self.f_to_c)
        self.f_to_c.grid(row=2, column=0)
        self.c_to_f = Button(self, text="<<", command=self.c_to_f)
        self.c_to_f.grid(row=2, column=1)

    def f_to_c(self):
        f = float(self.f_entry.get())
        c = (f - 32) * 5 / 9
        self.c_entry.delete(0, END)
        self.c_entry.insert(0, str(c))

    def c_to_f(self):
        c = float(self.c_entry.get())
        f = c * 9 / 5 + 32
        self.f_entry.delete(0, END)
        self.f_entry.insert(0, str(f))

app = ConvertTemp()
app.mainloop()

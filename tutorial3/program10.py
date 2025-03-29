# A bouncy program is defined as follows – The program computes and displays the total distance traveled by a ball, given three inputs—the initial height from which it is dropped, its bounciness index, and the number of bounces. Given the inputs write a GUI-based program to compute the total distance traveled.

import tkinter as tk
def calculate_distance():
    try:
        initial_height = float(initial_height_entry.get())
        bounciness_index = float(bounciness_index_entry.get())
        num_bounces = int(num_bounces_entry.get())

        if initial_height <= 0 or bounciness_index <= 0 or num_bounces <= 0:
            result_label.config(text="Invalid input. All values must be positive.")
            return

        total_distance = initial_height
        for i in range(num_bounces):
            total_distance += 2 * initial_height * (bounciness_index ** i)

        result_label.config(text=f"Total distance traveled: {total_distance:.2f}")

    except ValueError:
        result_label.config(text="Invalid input. Please enter valid numbers.")

window = tk.Tk()
window.title("Bouncing Ball Distance Calculator")

initial_height_label = tk.Label(window, text="Initial Height (meters):")
initial_height_label.grid(row=0, column=0, padx=5, pady=5)
initial_height_entry = tk.Entry(window)
initial_height_entry.grid(row=0, column=1, padx=5, pady=5)

bounciness_index_label = tk.Label(window, text="Bounciness Index (0-1):")
bounciness_index_label.grid(row=1, column=0, padx=5, pady=5)
bounciness_index_entry = tk.Entry(window)
bounciness_index_entry.grid(row=1, column=1, padx=5, pady=5)

num_bounces_label = tk.Label(window, text="Number of Bounces:")
num_bounces_label.grid(row=2, column=0, padx=5, pady=5)
num_bounces_entry = tk.Entry(window)
num_bounces_entry.grid(row=2, column=1, padx=5, pady=5)

calculate_button = tk.Button(window, text="Calculate", command=calculate_distance)
calculate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

result_label = tk.Label(window, text="")
result_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()
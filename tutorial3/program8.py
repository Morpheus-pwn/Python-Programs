# Write a GUI-based program that plays a guess-the-number game in which the user guesses a number between 1 and 100 and the computer provides the responses. The window should display the user’s guesses with a label by saying, “Too large, try again,” or “Too small, try again.” When the user finally guesses the correct number, the program congratulates him and tells him the total number of guesses.

import tkinter as tk
import random

def check_guess():
    global guesses
    guesses += 1

    try:
        guess = int(guess_entry.get())
        if guess < number:
            result_label.config(text="Too small, try again.")
        elif guess > number:
            result_label.config(text="Too large, try again.")
        else:
            result_label.config(text=f"Congratulations! You guessed it in {guesses} tries.")
            guess_entry.config(state="disabled")
            check_button.config(state="disabled")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

number = random.randint(1, 100)
guesses = 0

window = tk.Tk()
window.title("Guess the Number")

instructions_label = tk.Label(window, text="Guess a number between 1 and 100:")
instructions_label.pack()

guess_entry = tk.Entry(window)
guess_entry.pack()

check_button = tk.Button(window, text="Check", command=check_guess)
check_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()

window.mainloop()
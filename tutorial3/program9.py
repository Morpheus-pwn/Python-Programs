# Write a GUI-based program that plays a guess-the-number game in which the computer guesses a number between 1 and 100 and the user provides the responses. The window should display the computer’s guesses with a label. The user enters a hint in response, by selecting one of a set of command buttons labeled Too small, Too large, and Correct. When the game is over, you should disable these buttons and wait for the user to click New game, as before.

import tkinter as tk
import random

class GuessTheNumberGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        self.number_to_guess = random.randint(1, 100)
        self.current_guess = None
        self.guesses = 0
        
        self.instructions_label = tk.Label(master, text="Think of a number between 1 and 100.")
        self.instructions_label.pack()
        
        self.guess_label = tk.Label(master, text="")
        self.guess_label.pack()
        
        self.too_small_button = tk.Button(master, text="Too small", command=self.too_small)
        self.too_small_button.pack()
        
        self.too_large_button = tk.Button(master, text="Too large", command=self.too_large)
        self.too_large_button.pack()
        
        self.correct_button = tk.Button(master, text="Correct", command=self.correct)
        self.correct_button.pack()
        
        self.new_game_button = tk.Button(master, text="New Game", command=self.new_game, state="disabled")
        self.new_game_button.pack()

        self.start_new_game()

    def start_new_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.current_guess = random.randint(1, 100)
        self.guesses = 0
        self.guess_label.config(text=f"Computer guesses: {self.current_guess}")
        self.too_small_button.config(state="normal")
        self.too_large_button.config(state="normal")
        self.correct_button.config(state="normal")
        self.new_game_button.config(state="disabled")

    def too_small(self):
        self.guesses += 1
        self.current_guess += random.randint(1, (100 - self.current_guess) // 2)
        self.guess_label.config(text=f"Computer guesses: {self.current_guess}")

    def too_large(self):
        self.guesses += 1
        self.current_guess -= random.randint(1, (self.current_guess - 1) // 2)
        self.guess_label.config(text=f"Computer guesses: {self.current_guess}")

    def correct(self):
        self.guesses += 1
        self.guess_label.config(text=f"Computer guessed it in {self.guesses} tries!")
        self.too_small_button.config(state="disabled")
        self.too_large_button.config(state="disabled")
        self.correct_button.config(state="disabled")
        self.new_game_button.config(state="normal")

    def new_game(self):
        self.start_new_game()

root = tk.Tk()
game = GuessTheNumberGame(root)
root.mainloop()
import tkinter as tk
import random
def check_guess():
    global attempts
    guess = int(guess_entry.get())
    if guess < target_number:
        result_label.config(text="Too small, try again.")
    elif guess > target_number:
        result_label.config(text="Too large, try again.")
    else:
        result_label.config(text=f"Correct! You guessed in {attempts} attempts.")
        guess_button.config(state="disabled")
        attempts_label.config(text=f"Total Guesses: {attempts}")
window = tk.Tk()
window.title("Guess the Number")
target_number = random.randint(1, 100)
attempts = 0
instructions_label = tk.Label(window, text="Guess the number between 1 and 100:")
instructions_label.pack()
guess_entry = tk.Entry(window)
guess_entry.pack()
guess_button = tk.Button(window, text="Check Guess", command=lambda: [check_guess(), attempts := attempts + 1])
guess_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
attempts_label = tk.Label(window, text="Total Guesses: 0")
attempts_label.pack()
window.mainloop()

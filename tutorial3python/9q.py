import tkinter as tk
import random
def give_hint(hint):
    global low, high
    if hint == "Too small":
        low = guess + 1
    elif hint == "Too large":
        high = guess - 1
    elif hint == "Correct":
        result_label.config(text=f"Correct! The computer guessed {guess}.")
        hint_button1.config(state="disabled")
        hint_button2.config(state="disabled")
        new_game_button.config(state="normal")
    guess = random.randint(low, high)
    guess_label.config(text=f"Computer's Guess: {guess}")
def new_game():
    global low, high, guess
    low, high = 1, 100
    guess = random.randint(low, high)
    guess_label.config(text=f"Computer's Guess: {guess}")
    result_label.config(text="")
    hint_button1.config(state="normal")
    hint_button2.config(state="normal")
    new_game_button.config(state="disabled")
window = tk.Tk()
window.title("Computer Guessing Game")
low, high = 1, 100
guess = random.randint(low, high)
guess_label = tk.Label(window, text=f"Computer's Guess: {guess}")
guess_label.pack()
hint_button1 = tk.Button(window, text="Too small", command=lambda: give_hint("Too small"))
hint_button1.pack()
hint_button2 = tk.Button(window, text="Too large", command=lambda: give_hint("Too large"))
hint_button2.pack()
hint_button3 = tk.Button(window, text="Correct", command=lambda: give_hint("Correct"))
hint_button3.pack()
new_game_button = tk.Button(window, text="New Game", command=new_game, state="disabled")
new_game_button.pack()
result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()

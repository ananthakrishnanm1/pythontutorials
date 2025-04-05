import tkinter as tk
import math
def compute_square_root():
    try:
        number = int(input_entry.get())
        result = math.sqrt(number)
        result_label.config(text="Square Root: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")
window = tk.Tk()
window.title("Square Root Calculator")
input_label = tk.Label(window, text="Enter Integer:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()
compute_button = tk.Button(window, text="Compute", command=compute_square_root)
compute_button.pack()
result_label = tk.Label(window, text="Square Root: ")
result_label.pack()
window.mainloop()

import tkinter as tk

def calculate_distance():
    try:
        height = float(height_entry.get())
        bounciness = float(bounciness_entry.get())
        bounces = int(bounces_entry.get())
        total_distance = height
        current_height = height * bounciness
        for _ in range(bounces):
            total_distance += 2 * current_height
            current_height *= bounciness
        total_distance_label.config(text=f"Total Distance: {total_distance} meters")
    except ValueError:
        total_distance_label.config(text="Invalid input, please enter valid numbers.")

window = tk.Tk()
window.title("Bouncy Ball Distance Calculator")

height_label = tk.Label(window, text="Initial Height (m):")
height_label.pack()
height_entry = tk.Entry(window)
height_entry.pack()

bounciness_label = tk.Label(window, text="Bounciness Index:")
bounciness_label.pack()
bounciness_entry = tk.Entry(window)
bounciness_entry.pack()

bounces_label = tk.Label(window, text="Number of Bounces:")
bounces_label.pack()
bounces_entry = tk.Entry(window)
bounces_entry.pack()

calculate_button = tk.Button(window, text="Calculate", command=calculate_distance)
calculate_button.pack()

total_distance_label = tk.Label(window, text="Total Distance: ")
total_distance_label.pack()

window.mainloop()

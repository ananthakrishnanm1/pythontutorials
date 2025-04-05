import tkinter as tk
def fahrenheit_to_celsius():
    fahrenheit = float(fahrenheit_entry.get())
    celsius = (fahrenheit - 32) * 5.0/9.0
    celsius_entry.delete(0, tk.END)
    celsius_entry.insert(0, str(round(celsius, 2)))
def celsius_to_fahrenheit():
    celsius = float(celsius_entry.get())
    fahrenheit = (celsius * 9.0/5.0) + 32
    fahrenheit_entry.delete(0, tk.END)
    fahrenheit_entry.insert(0, str(round(fahrenheit, 2)))
window = tk.Tk()
window.title("Temperature Converter")
fahrenheit_label = tk.Label(window, text="Fahrenheit")
fahrenheit_label.grid(row=0, column=0)
celsius_label = tk.Label(window, text="Celsius")
celsius_label.grid(row=1, column=0)
fahrenheit_entry = tk.Entry(window)
fahrenheit_entry.grid(row=0, column=1)
fahrenheit_entry.insert(0, "32")
celsius_entry = tk.Entry(window)
celsius_entry.grid(row=1, column=1)
celsius_entry.insert(0, "0.0")
button1 = tk.Button(window, text=">>>>", command=fahrenheit_to_celsius)
button1.grid(row=2, column=0)
button2 = tk.Button(window, text="<<<<", command=celsius_to_fahrenheit)
button2.grid(row=2, column=1)
window.mainloop()

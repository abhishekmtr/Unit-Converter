import tkinter as tk
from tkinter import messagebox

def calculate_area():
    try:
        base = float(entry_base.get())
        height = float(entry_height.get())
        area = 0.5 * base * height
        label_result.config(text=f"Area: {area:.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers")

# Create GUI window
root = tk.Tk()
root.title("Triangle Area Calculator")
root.geometry("300x200")

# Base input
tk.Label(root, text="Base:").pack(pady=5)
entry_base = tk.Entry(root)
entry_base.pack()

# Height input
tk.Label(root, text="Height:").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack()

# Calculate button
btn_calc = tk.Button(root, text="Calculate Area", command=calculate_area)
btn_calc.pack(pady=10)

# Result label
label_result = tk.Label(root, text="Area: ")
label_result.pack(pady=10)

root.mainloop()

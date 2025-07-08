import tkinter as tk
from tkinter import messagebox

def calculate(operator):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ValueError("Cannot divide by zero")
            result = num1 / num2
        else:
            result = "Unknown operator"

        result_label.config(text="Result: " + str(result))

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))


# GUI Window
root = tk.Tk()
root.title("Python Calculator")
root.geometry("300x250")

# Input Fields
tk.Label(root, text="Enter first number").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Enter second number").pack()
entry2 = tk.Entry(root)
entry2.pack()

# Buttons
frame = tk.Frame(root)
frame.pack(pady=10)

tk.Button(frame, text='+', width=5, command=lambda: calculate('+')).grid(row=0, column=0)
tk.Button(frame, text='-', width=5, command=lambda: calculate('-')).grid(row=0, column=1)
tk.Button(frame, text='×', width=5, command=lambda: calculate('*')).grid(row=0, column=2)
tk.Button(frame, text='÷', width=5, command=lambda: calculate('/')).grid(row=0, column=3)

# Result Display
result_label = tk.Label(root, text="Result:", font=("Arial", 14))
result_label.pack(pady=20)

# Run the App
root.mainloop()

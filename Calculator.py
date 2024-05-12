import tkinter as tk
from tkinter import messagebox

import math

def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 + num2
        lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 - num2
        lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 * num2
        lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        if num2 == 0:
            messagebox.showerror("Error", "Division by zero is not allowed.")
        else:
            result = num1 / num2
            lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def exponentiate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        result = num1 ** num2
        lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

def square_root():
    try:
        num = float(entry_num.get())
        if num < 0:
            messagebox.showerror("Error", "Cannot calculate square root of a negative number.")
        else:
            result = math.sqrt(num)
            lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

def factorial():
    try:
        num = int(entry_num.get())
        if num < 0:
            messagebox.showerror("Error", "Cannot calculate factorial of a negative number.")
        else:
            result = math.factorial(num)
            lbl_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid integer.")

root = tk.Tk()
root.title("Advanced Calculator")

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

entry_num = tk.Entry(root)
entry_num.grid(row=2, column=1)

lbl_num1 = tk.Label(root, text="Number 1:")
lbl_num1.grid(row=0, column=0)

lbl_num2 = tk.Label(root, text="Number 2:")
lbl_num2.grid(row=1, column=0)

lbl_num = tk.Label(root, text="Number:")
lbl_num.grid(row=2, column=0)

lbl_result = tk.Label(root, text="Result:")
lbl_result.grid(row=4, column=0, columnspan=2)

btn_add = tk.Button(root, text="Add", command=add)
btn_add.grid(row=3, column=0)

btn_subtract = tk.Button(root, text="Subtract", command=subtract)
btn_subtract.grid(row=3, column=1)

btn_multiply = tk.Button(root, text="Multiply", command=multiply)
btn_multiply.grid(row=3, column=2)

btn_divide = tk.Button(root, text="Divide", command=divide)
btn_divide.grid(row=3, column=3)

btn_exponentiate = tk.Button(root, text="Exponentiate", command=exponentiate)
btn_exponentiate.grid(row=3, column=4)

btn_square_root = tk.Button(root, text="Square Root", command=square_root)
btn_square_root.grid(row=3, column=5)

btn_factorial = tk.Button(root, text="Factorial", command=factorial)
btn_factorial.grid(row=3, column=6)

root.mainloop()

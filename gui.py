#!/usr/bin/env python3

import tkinter as tk

root = tk.Tk()
root.title("Python 3 GUI Calculator")

entry = tk.Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

def button_click(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, tk.END)

def button_add():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "addition"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_subtract():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "subtraction"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_multiply():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "multiplication"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_divide():
    first_number = entry.get()
    global f_num
    global math_operation
    math_operation = "division"
    f_num = int(first_number)
    entry.delete(0, tk.END)

def button_equal():
    second_number = entry.get()
    entry.delete(0, tk.END)

    if math_operation == "addition":
        entry.insert(0, f_num + int(second_number))
    elif math_operation == "subtraction":
        entry.insert(0, f_num - int(second_number))
    elif math_operation == "multiplication":
        entry.insert(0, f_num * int(second_number))
    elif math_operation == "division":
        entry.insert(0, f_num / int(second_number))

# Define the calculator buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = tk.Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = tk.Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = tk.Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = tk.Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = tk.Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = tk.Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = tk.Button(root, text="+", padx=40, pady=20, command=button_add)
button_subtract = tk.Button(root, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=40, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=40, pady=20, command=button_divide)
button_equal = tk.Button(root, text="=", padx=40, pady=20, command=button_equal)
button_clear = tk.Button(root, text="C", padx=40, pady=20, command=button_clear)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3)
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)
button_7.grid(row=5, column=0)
button_8.grid(row=5, column=1)
button_9.grid(row=5, column=2)
button_multiply.grid(row=5, column=3)
button_clear.grid(row=6, column=0)
button_0.grid(row=6, column=1)
button_equal.grid(row=6, column=2)
button_divide.grid(row=6, column=3)

def main() -> None:
    root.mainloop()
    
if __name__ == "__main__":
    main()

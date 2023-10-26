'''
Calculator.py
program a calculator with a GUI using python
'''

import tkinter as tk

calculation = ""

# create functions


def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation = str(eval(calculation))
        result_text.delete(1.0, tk.END)
        result_text.insert(1.0, calculation)
    except:
        clear_calculation()
        result_text.insert(1.0, "Error")


def clear_calculation():
    global calculation
    calculation = ""
    result_text.delete(1.0, tk.END)


# create GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("350x300")

result_text = tk.Text(root, height=2, width=20, font=("Arial", 24))
result_text.grid(columnspan=5)

# create buttons
# button 1
button_1 = tk.Button(
    root, text="1", command=lambda: add_to_calculation(1), height=2, width=7)
button_1.grid(row=2, column=0)

# button 2
button_2 = tk.Button(
    root, text="2", command=lambda: add_to_calculation(2), height=2, width=7)
button_2.grid(row=2, column=1)

# button 3
button_3 = tk.Button(
    root, text="3", command=lambda: add_to_calculation(3), height=2, width=7)
button_3.grid(row=2, column=2)

# button 4
button_4 = tk.Button(
    root, text="4", command=lambda: add_to_calculation(4), height=2, width=7)
button_4.grid(row=3, column=0)

# button 5
button_5 = tk.Button(
    root, text="5", command=lambda: add_to_calculation(5), height=2, width=7)
button_5.grid(row=3, column=1)

# button 6
button_6 = tk.Button(
    root, text="6", command=lambda: add_to_calculation(6), height=2, width=7)
button_6.grid(row=3, column=2)

# button 7
button_7 = tk.Button(
    root, text="7", command=lambda: add_to_calculation(7), height=2, width=7)
button_7.grid(row=4, column=0)

# button 8
button_8 = tk.Button(
    root, text="8", command=lambda: add_to_calculation(8), height=2, width=7)
button_8.grid(row=4, column=1)

# button 9
button_9 = tk.Button(
    root, text="9", command=lambda: add_to_calculation(9), height=2, width=7)
button_9.grid(row=4, column=2)

# button 0
button_0 = tk.Button(
    root, text="0", command=lambda: add_to_calculation(0), height=2, width=7)
button_0.grid(row=5, column=1)

# button left parenthesis
button_left_parenthesis = tk.Button(
    root, text="(", command=lambda: add_to_calculation("("), height=2, width=7)
button_left_parenthesis.grid(row=5, column=0)

# button right parenthesis
button_right_parenthesis = tk.Button(
    root, text=")", command=lambda: add_to_calculation(")"), height=2, width=7)
button_right_parenthesis.grid(row=5, column=2)

# button decimal
button_decimal = tk.Button(
    root, text=".", command=lambda: add_to_calculation("."), height=2, width=7)
button_decimal.grid(row=6, column=0)

# button negative
button_negative = tk.Button(
    root, text="\-", command=lambda: add_to_calculation("-"), height=2, width=7)
button_negative.grid(row=6, column=2)

# button add
button_add = tk.Button(
    root, text="+", command=lambda: add_to_calculation("+"), height=2, width=7)
button_add.grid(row=2, column=3)

# button subtract
button_subtract = tk.Button(
    root, text="-", command=lambda: add_to_calculation("-"), height=2, width=7)
button_subtract.grid(row=3, column=3)

# button multiply
button_multiply = tk.Button(
    root, text="*", command=lambda: add_to_calculation("*"), height=2, width=7)
button_multiply.grid(row=4, column=3)

# button divide
button_divide = tk.Button(
    root, text="/", command=lambda: add_to_calculation("/"), height=2, width=7)
button_divide.grid(row=5, column=3)

# button clear
button_clear = tk.Button(
    root, text="CE", command=clear_calculation, height=2, width=7)
button_clear.grid(row=6, column=1)

# button equals
button_equals = tk.Button(
    root, text="=", command=evaluate_calculation, height=2, width=7)
button_equals.grid(row=6, column=3)

root.mainloop()

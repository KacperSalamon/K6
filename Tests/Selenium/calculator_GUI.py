from glob import glob
import tkinter as tk
from unittest import result

calculation = ""

def addCalculation(sym):
    global calculation
    calculation += str(sym)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)
    

def evaluateCalc():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ""
        textResult.delete(1.0, "end")
        textResult.insert(1.0, result)
    except:
        clearField()
        textResult.insert(1.0, "Wrong calculation/s")

def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")


root = tk.Tk()
root.geometry("300x275")

textResult = tk.Text(root, height=2, width=16, font=("Arial", 24))
textResult.grid(columnspan=5)

button_one = tk.Button(root, text="1", command=lambda: addCalculation(1), width=5, font=("Arial", 14))
button_one.grid(row=2, column=1)
button_two = tk.Button(root, text="2", command=lambda: addCalculation(2), width=5, font=("Arial", 14))
button_two.grid(row=2, column=2)
button_three = tk.Button(root, text="3", command=lambda: addCalculation(3), width=5, font=("Arial", 14))
button_three.grid(row=2, column=3)
button_four = tk.Button(root, text="4", command=lambda: addCalculation(4), width=5, font=("Arial", 14))
button_four.grid(row=3, column=1)
button_five = tk.Button(root, text="5", command=lambda: addCalculation(5), width=5, font=("Arial", 14))
button_five.grid(row=3, column=2)
button_six = tk.Button(root, text="6", command=lambda: addCalculation(6), width=5, font=("Arial", 14))
button_six.grid(row=3, column=3)
button_seven = tk.Button(root, text="7", command=lambda: addCalculation(7), width=5, font=("Arial", 14))
button_seven.grid(row=4, column=1)
button_eight = tk.Button(root, text="8", command=lambda: addCalculation(8), width=5, font=("Arial", 14))
button_eight.grid(row=4, column=2)
button_nine = tk.Button(root, text="9", command=lambda: addCalculation(9), width=5, font=("Arial", 14))
button_nine.grid(row=4, column=3)
button_plus = tk.Button(root, text="+", command=lambda: addCalculation("+"), width=5, font=("Arial", 14))
button_plus.grid(row=2, column=4)
button_minus = tk.Button(root, text="-", command=lambda: addCalculation("-"), width=5, font=("Arial", 14))
button_minus.grid(row=3, column=4)
button_multi = tk.Button(root, text="*", command=lambda: addCalculation("*"), width=5, font=("Arial", 14))
button_multi.grid(row=5, column=4)
button_division = tk.Button(root, text="/", command=lambda: addCalculation("/"), width=5, font=("Arial", 14))
button_division.grid(row=4, column=4)
button_open_bracket = tk.Button(root, text="(", command=lambda: addCalculation("("), width=5, font=("Arial", 14))
button_open_bracket.grid(row=5, column=1)
button_close_bracket = tk.Button(root, text=")", command=lambda: addCalculation(")"), width=5, font=("Arial", 14))
button_close_bracket.grid(row=5, column=3)
button_zero = tk.Button(root, text="0", command=lambda: addCalculation(0), width=5, font=("Arial", 14))
button_zero.grid(row=5, column=2)
button_division = tk.Button(root, text="/", command=lambda: addCalculation("/"), width=5, font=("Arial", 14))
button_division.grid(row=4, column=4)
button_equal = tk.Button(root, text="=", command=evaluateCalc, width=11, font=("Arial", 14))
button_equal.grid(row=6, column=3, columnspan=2)
button_clear = tk.Button(root, text="C", command=clearField, width=11, font=("Arial", 14))
button_clear.grid(row=6, column=1, columnspan=2)
root.mainloop()
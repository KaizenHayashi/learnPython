# importing only those functions which are needed
import tkinter as tk

calculation = ""


def add_to_calc(symbol):
    global calculation
    calculation += str(symbol)
    # hyperspecific start and end, to delete the results of text box
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)


def evaluate_calculation():
    global calculation
    try:
        # Don't use eval function if the file needs to be online.
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        # This is same as line 21
        clear_field()
        text_result.insert(1.0, "Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# Creating tkinter window
root = tk.Tk()
# Specify title of project
root.title("Simple Calculator v1.0")
# Specify size of window
root.geometry("290x275")

text_result = tk.Text(root, bg="#000000", fg="lime", height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=4)

# lambda function refers to a function when it is called, instead of immediately calling it
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calc(1), width=5, font=("Courier", 14))
btn_1.grid(row=5, column=0)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calc(2), width=5, font=("Courier", 14))
btn_2.grid(row=5, column=1)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calc(3), width=5, font=("Courier", 14))
btn_3.grid(row=5, column=2)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calc(4), width=5, font=("Courier", 14))
btn_4.grid(row=4, column=0)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calc(5), width=5, font=("Courier", 14))
btn_5.grid(row=4, column=1)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calc(6), width=5, font=("Courier", 14))
btn_6.grid(row=4, column=2)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calc(7), width=5, font=("Courier", 14))
btn_7.grid(row=3, column=0)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calc(8), width=5, font=("Courier", 14))
btn_8.grid(row=3, column=1)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calc(9), width=5, font=("Courier", 14))
btn_9.grid(row=3, column=2)
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calc(0), width=12, font=("Courier", 14))
btn_0.grid(row=6, column=0, columnspan=2)

btn_add = tk.Button(root, text="+", command=lambda: add_to_calc("+"), width=5, font=("Courier", 14))
btn_add.grid(row=5, column=3)
btn_sub = tk.Button(root, text="-", command=lambda: add_to_calc("-"), width=5, font=("Courier", 14))
btn_sub.grid(row=4, column=3)
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calc("*"), width=5, font=("Courier", 14))
btn_mul.grid(row=3, column=3)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calc("/"), width=5, font=("Courier", 14))
btn_div.grid(row=2, column=3)
btn_dot = tk.Button(root, text=".", command=lambda: add_to_calc("."), width=5, font=("Courier", 14))
btn_dot.grid(row=6, column=2)

btn_opn = tk.Button(root, text="(", command=lambda: add_to_calc("("), width=5, font=("Courier", 14))
btn_opn.grid(row=2, column=1)
btn_cls = tk.Button(root, text=")", command=lambda: add_to_calc(")"), width=5, font=("Courier", 14))
btn_cls.grid(row=2, column=2)

btn_equal = tk.Button(root, text="=", command=evaluate_calculation, width=5, font=("Courier", 14))
btn_equal.grid(row=6, column=3)
# Use lambda when you have parentheses which is CALLING and not PASSING the function
btn_clear = tk.Button(root, text="C", command=clear_field, width=5, font=("Courier", 14))
btn_clear.grid(row=2, column=0)

# Execute Tkinter
root.mainloop()

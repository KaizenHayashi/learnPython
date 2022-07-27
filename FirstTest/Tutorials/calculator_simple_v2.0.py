# importing everything from tkinter
from tkinter import *


def btn_click(num):
    global val
    val += str(num)
    calculation.set(val)


def btn_clear():
    global val
    val = ""
    calculation.set("")


def btn_equals():
    global val
    # Beware of using eval function if file is linked online
    result = str(round((eval(val)), 5))
    val = result
    calculation.set(result)


# Creating tkinter window
root = Tk()
# Specify title of project
root.title("Simple Calculator v2.0")
# Specify size of window, and then location of startup
root.geometry("298x330+300+100")

val = ""
calculation = StringVar()

display = Entry(root, textvariable=calculation, bd=20, justify="right", bg="#8fb2c4", disabledbackground="#8fb2c4", disabledforeground="black", font=("Fixedsys", 17), width=16)
display.grid(row=0, columnspan=4)
display.config(state=DISABLED)

# lambda function refers to a function when it is called, instead of immediately calling it
# Use lambda when you have parentheses which is CALLING and not PASSING the function
btn_C = Button(root, text="C", font=("Courier", 13, "bold"), bd=10, bg="orange", activebackground="brown", width=4, command=lambda: btn_clear())
btn_C.grid(row=1, column=0)
btn_opn = Button(root, text="(", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click("("))
btn_opn.grid(row=1, column=1)
btn_cls = Button(root, text=")", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(")"))
btn_cls.grid(row=1, column=2)

btn_div = Button(root, text="/", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click("/"))
btn_div.grid(row=1, column=3)
btn_mul = Button(root, text="*", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click("*"))
btn_mul.grid(row=2, column=3)
btn_sub = Button(root, text="-", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click("-"))
btn_sub.grid(row=3, column=3)
btn_add = Button(root, text="+", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click("+"))
btn_add.grid(row=4, column=3)

btn_eql = Button(root, text="=", font=("Courier", 13, "bold"), bd=10, bg="#8fb2c4", activebackground="#5f8294", width=4, command=lambda: btn_equals())
btn_eql.grid(row=5, column=3)

btn_dot = Button(root, text=".", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click("."))
btn_dot.grid(row=5, column=2)

btn_0 = Button(root, text="0", font=("Courier", 13, "bold"), bd=10, width=11, command=lambda: btn_click(0))
btn_0.grid(row=5, column=0, columnspan=2)

btn_1 = Button(root, text="1", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(1))
btn_1.grid(row=4, column=0)
btn_2 = Button(root, text="2", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(2))
btn_2.grid(row=4, column=1)
btn_3 = Button(root, text="3", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(3))
btn_3.grid(row=4, column=2)

btn_4 = Button(root, text="4", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(4))
btn_4.grid(row=3, column=0)
btn_5 = Button(root, text="5", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(5))
btn_5.grid(row=3, column=1)
btn_6 = Button(root, text="6", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(6))
btn_6.grid(row=3, column=2)

btn_7 = Button(root, text="7", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(7))
btn_7.grid(row=2, column=0)
btn_8 = Button(root, text="8", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(8))
btn_8.grid(row=2, column=1)
btn_9 = Button(root, text="9", font=("Courier", 13, "bold"), bd=10, width=4, command=lambda: btn_click(9))
btn_9.grid(row=2, column=2)

# Execute Tkinter
root.mainloop()

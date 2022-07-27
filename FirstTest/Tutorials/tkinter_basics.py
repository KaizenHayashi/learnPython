# importing everything from tkinter
from tkinter import *

# generate window
root = Tk()

# Specify title of project
root.title("Tkinter Basics")
# Specify size of window, and then location of startup
root.geometry("700x500+300+100")

# creating a label widget
lbl1 = Label(root, text="Hello World!").grid(row=0, column=0)
lbl2 = Label(root, text="Hello World!").grid(row=0, column=1)
lbl3 = Label(root, text="Hewwo Wowwd owo", wraplength=70).grid(row=1, column=0)


def gen_text():
    lbl4 = Label(root, text="Why are you pushing my buttons?")
    lbl4.grid(row=2, column=0)


# creating button widgets
btn1 = Button(root, text="Raised", bd=5, width=5, relief="raised", bg="red", activebackground="red3",
              command=lambda: gen_text())
btn1.grid(row=3, column=0, columnspan=1)
btn2 = Button(root, text="Sunken", bd=5, width=5, relief="sunken", bg="orange", activebackground="orange3")
btn2.grid(row=3, column=1, columnspan=1)
btn3 = Button(root, text="Flat", bd=5, width=5, relief="flat", bg="yellow", activebackground="yellow3")
btn3.grid(row=4, column=0, columnspan=1)
btn4 = Button(root, text="Ridge", bd=5, width=5, relief="ridge", bg="green2", activebackground="green3")
btn4.grid(row=4, column=1, columnspan=1)
btn5 = Button(root, text="Solid", bd=5, width=5, relief="solid", bg="cyan", activebackground="cyan3")
btn5.grid(row=5, column=0, columnspan=1)
btn6 = Button(root, text="Groove", bd=5, width=5, relief="groove", bg="orchid1", activebackground="orchid2")
btn6.grid(row=5, column=1, columnspan=1)

# shoving it onto the screen
# Pack allows things to be on 1 row or 1 column
# myLabel1.pack()

# Grid makes grids

lbl5 = Label(root, text="Insert your name")
lbl5.grid(row=6, column=0, columnspan=2)
entry1 = Entry(root, width=20, bg="pink1", fg="gray10", bd=7)
entry1.grid(row=7, column=0, columnspan=2)
entry1.insert(0, "Default Dan")


def submit_name():
    # Shows result
    display_name = "Hello " + entry1.get() + ".\n"
    name_word = Label(root, text=display_name)
    name_word.grid(row=9, column=0, columnspan=2)
    # Clears entry
    entry1.delete(0, END)


submitBtn = Button(root, text="Submit", command=lambda: submit_name())
submitBtn.grid(row=8, column=0, columnspan=2)

# looping the program
root.mainloop()

from tkinter import *

root = Tk()

mylabel = Label(root, text="Hello world")
mylabel2 = Label(root, text="Hello world!")

mybutton = Button(root, text="close", fg="white", bg="pink")


mybutton.grid(row=1, column=1)
mylabel.grid(row=0, column=0)
mylabel2.grid(row=2, column=2)


root.mainloop()

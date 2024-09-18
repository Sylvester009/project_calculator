from tkinter import *

root = Tk()

#Input
inputentry = Entry()

# Number 
button1 = Button(root, text="1", fg="white", bg="gray")
button2 = Button(root, text="2", fg="white", bg="gray")
button3 = Button(root, text="3", fg="white", bg="gray")
button4 = Button(root, text="4", fg="white", bg="gray")
button5 = Button(root, text="5", fg="white", bg="gray")
button6 = Button(root, text="6", fg="white", bg="gray")
button7 = Button(root, text="7", fg="white", bg="gray")
button8 = Button(root, text="8", fg="white", bg="gray")
button9 = Button(root, text="9", fg="white", bg="gray")
button0 = Button(root, text="0", fg="white", bg="gray")
button00 = Button(root, text="00", fg="white", bg="gray")
buttondot = Button(root, text=".", fg="white", bg="gray")

# arithmetic symbols
buttonplus = Button(root, text=" + ", fg="white", bg="gray")
buttonminus = Button(root, text=" - ", fg="white", bg="gray")
buttontimes = Button(root, text=" x ", fg="white", bg="gray")
buttondivide = Button(root, text=" / ", fg="white", bg="gray")
buttonequal = Button(root, text=" = ", fg="white", bg="gray")
buttonsquare = Button(root, text=" x^2 ", fg="white", bg="gray")
buttonsqroot = Button(root, text=" x^1/2 ", fg="white", bg="gray")
buttoncube = Button(root, text=" x^3 ", fg="white", bg="gray")


# Render to Window

# input
inputentry.grid(row=0, column=0)

# Nummber rendering
button1.grid(row=1, column=2)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0)
button4.grid(row=3, column=0)
button5.grid(row=4, column=0)
button6.grid(row=5, column=0)
button7.grid(row=6, column=0)
button8.grid(row=7, column=0)
button9.grid(row=8, column=0)
button0.grid(row=9, column=0)
button00.grid(row=10, column=0)
buttondot.grid(row=11, column=0)

# arithmetic symbols
buttonplus.grid(row=0, column=1)
buttonminus.grid(row=1, column=1)
buttontimes.grid(row=2, column=1)
buttondivide.grid(row=3, column=1)
buttonequal.grid(row=4, column=1)
buttonsquare.grid(row=5, column=1)
buttonsqroot.grid(row=6, column=1)
buttoncube.grid(row=7, column=1)



root.mainloop()

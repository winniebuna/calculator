# from tkinter import*
# from tkinter import messagebox
#
#
# def helloCallBack():
#     messagebox.showinfo("Winnie window", "hello winnie")
#
# window = Tk()
# btn = Button(window, text="hello", command=helloCallBack)
# btn.place(bordermode=OUTSIDE, height=100, width=100)
#
# window.mainloop()

from tkinter import *


def add():
    x=fn.get()
    y=sn.get()
    r=int(x)+int(y)
    relt.config(text=r)

def sub():
    x=fn.get()
    y=sn.get()
    r=int(x)-int(y)
    relt.config(text=r)


def mul():
    x=fn.get()
    y=sn.get()
    r=int(x)*int(y)
    relt.config(text=r)


def div():
    x=fn.get()
    y=sn.get()
    r=int(x)/int(y)
    relt.config(text=r)


window = Tk()
lbl = Label(window, text='Arithmetic Calculator ')
lbl.grid(row=0, columnspan=4)

fNum = Label(window, text='First Number: ')
fNum.grid(row=1, column=0)

fn = Entry(window)
fn.grid(row=1, column=4)

sNum = Label(window, text='Second Number: ')
sNum.grid(row=2, column=0)

sn = Entry(window)
sn.grid(row=2, column=4)

result = Label(window, text='Result: ')
result.grid(row=3, column=0)

relt = Label(window)
relt.grid(row=3, column=4)

btnSubmit = Button(window, text="Add", command=add)
btnSubmit.grid(row=4, column=0)

btnSubmit = Button(window, text="Subtract", command=sub)
btnSubmit.grid(row=4, column=2)

btnSubmit = Button(window, text="Multiply", command=mul)
btnSubmit.grid(row=4, column=4)

btnSubmit = Button(window, text="Divide", command=div)
btnSubmit.grid(row=4, column=6)

window.mainloop()
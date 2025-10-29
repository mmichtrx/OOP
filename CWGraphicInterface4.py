#Calculator
import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x500")

answer = Text(width=35, height=2)
answer.place(x=100, y=100)

def show(self,x):
    try:
        if x == "0":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.instert(tk.INSERT,x)
            answer.insert(tk.INSERT, final_answer)

        else:
            answer.insert(tk.INSERT, x)

        if x == "C":
            answer.delete(1.0, END)

    except:
        answer.delete(1.0, END)


B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=100, y=150)

B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=200, y=150)

Badd = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
Badd.place(x=300, y=150)

Bsub = Button(top, text="-", width=10, height=5, command=lambda: show("-"))
Bsub.place(x=100, y=250)

Bmul = Button(top, text="*", width=10, height=5, command=lambda: show("*"))
Bmul.place(x=200, y=250)

Bdiv = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
Bdiv.place(x=300, y=250)

Bclear = Button(top, text="Clear", width=10, height=5, command=lambda: show("Clear"))
Bclear.place(x=100, y=350)

top.mainloop()
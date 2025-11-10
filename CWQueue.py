import tkinter as tk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self):
        self.element.append(x)

    def dequeue(self):
       if self.element:
            return self.element.pop(0)
        return None

    def displayQueue(self):
        return self.element

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


Bq = Button(top, text="Queue", width=10, height=5, command=lambda: show("Queue"))
Bq.place(x=100, y=150)

Beq = Button(top, text="Enqueue", width=10, height=5, command=lambda: show("Enqueue"))
Beq.place(x=200, y=150)

Bdq = Button(top, text="Dequeue", width=10, height=5, command=lambda: show("Dequeue"))
Bdq.place(x=300, y=150)

Bdisq = Button(top, text="DisplayQueue", width=10, height=5, command=lambda: show("DisplayQueue"))
Bdisq.place(x=100, y=250)

top.mainloop()


q1 = Queue()
q2 = Queue()
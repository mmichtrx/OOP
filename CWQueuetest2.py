import tkinter as tk
from tkinter import *

class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, x):
        self.element.append(x)

    def dequeue(self):
        if self.element:
            return self.element.pop(0)
        return None

    def displayQueue(self):
        return self.element

top = Tk()
top.geometry("500x500")
top.title("Queue Example")


q1 = Queue()


answer = Text(top, width=35, height=5)
answer.place(x=100, y=50)

def enqueue_action():
    text = answer.get("1.0", "end-1c").strip()
    if text:
        q1.enqueue(text)
        answer.delete("1.0", END)
        answer.insert(END, f"Enqueued: {text}")

def dequeue_action():
    item = q1.dequeue()
    answer.delete("1.0", END)
    if item:
        answer.insert(END, f"Dequeued: {item}")
    else:
        answer.insert(END, "Queue is empty")

def display_action():
    answer.delete("1.0", END)
    answer.insert(END, "Queue contents:\n")
    for i, item in enumerate(q1.displayQueue(), start=1):
        answer.insert(END, f"{i}. {item}\n")


Beq = Button(top, text="Enqueue", width=10, height=2, command=enqueue_action)
Beq.place(x=100, y=150)

Bdq = Button(top, text="Dequeue", width=10, height=2, command=dequeue_action)
Bdq.place(x=200, y=150)

Bdisq = Button(top, text="DisplayQueue", width=12, height=2, command=display_action)
Bdisq.place(x=300, y=150)

top.mainloop()
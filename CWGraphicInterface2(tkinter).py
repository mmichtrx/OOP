import tkinter

root = tkinter.Tk()
root.resizable(False,False)

#createcanvas
myCanvas = tkinter.Canvas(root, bg="white", height=500, width=800)

shapel1 = myCanvas.create_oval(200,250,600,500, fill="green")
shapel2 = myCanvas.create_arc(122,244,600,300, fill="blue")
shapel3 = myCanvas.create_rectangle(180,200,300,300, fill="yellow")
shapel4 = myCanvas.create_polygon(200,250,300,600, fill="green")




myCanvas.pack()
root.mainloop()
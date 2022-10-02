import tkinter
from tkinter import messagebox

top=tkinter.Tk()

def hellocallback():
    messagebox.showinfo("hello python","hello world")

b=tkinter.Button(top,text="hello",command=hellocallback)
b.pack()
top.mainloop()

import tkinter
from tkinter import *

class App:
        def __init__(self,m1):
                self.s=0
                self.b=""
                self.master=m1
                self.m=Menu(self.master)
                self.master.config(menu=self.m)
                self.f=Menu(self.m)
                self.m.add_cascade(label="File",menu=self.f)
                self.o=Menu(self.f)
                self.f.add_command(label="New",command=self.window)
                self.f.add_command(label="Exit",command=self.master.quit)
                self.master.mainloop()
        def gx(self):
                self.s=int(self.t1.get())
                self.b=""
                while self.s>0:
                    self.b=str(self.s%2)+self.b
                    self.s=self.s//2
                self.t2.set(self.b)
                             
        def window(self):
                self.t1=StringVar() 
                self.t2=StringVar()
                self.s1=Label(self.master,text="decimal number: ")
                self.s2=Entry(self.master,width=30,textvariable=self.t1)
                self.s3=Label(self.master,text="Binary : ")
                self.s4=Entry(self.master,width=50,textvariable=self.t2)
                self.button1=Button(self.master,text="Check:",fg="blue",command=self.gx)
                self.button2=Button(self.master,text="Quit",fg="red",command=quit)
                self.s1.grid(row=1,column=1)
                self.s2.grid(row=1,column=2)
                self.s3.grid(row=2,column=1)
                self.s4.grid(row=2,column=2)
                self.button1.grid(row=3,column=1)
                self.button2.grid(row=3,column=2)
                



h=App(Tk())

                


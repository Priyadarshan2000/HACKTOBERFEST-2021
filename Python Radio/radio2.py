import tkinter as tk
from tkinter import messagebox

def disp():
    x=int(k.get())
    
    if x==1:
        n=int(t1.get())
        u=""
        while n>0:
            u=str(n%2)+u
            n=n//2
        t2.set(u)    
    elif x==2:
        q=t1.get()
        bin=""
        p=len(q)-1
        dec=0
        for i in range(0,len(q)):
            if q[i]=="1":
                dec+=(2**p)
            p=p-1    
        t2.set(dec)

        
root=tk.Tk()
k=tk.StringVar()
t1=tk.StringVar()
t2=tk.StringVar()
        
g=tk.Label(root,text="Converter").pack()


r2=tk.Label(root,text="1. Enter A Number :")
r2.pack()
r3=tk.Entry(root,width=30,textvariable=t1)
r3.pack()

r1=tk.Label(root,text="2. Choose A Base:")
r1.pack()

tk.Radiobutton(root,
               text="To Binary",
               padx=20,
               variable=k,
               value=1).pack(anchor=tk.W)

tk.Radiobutton(root,
               text="To Decimal",
               padx=20,
               variable=k,
               value=2).pack(anchor=tk.W)

r4=tk.Label(root,text="Output :")
r4.pack()

r5=tk.Entry(root,width=30,textvariable=t2)
r5.pack()

tk.Button(root,text="OK",command=disp).pack(anchor=tk.W)

root.mainloop()
               

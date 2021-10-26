from tkinter import *

def fx():
    z.set(country.get())
    

root=Tk()

    
country=StringVar()
z=StringVar()

s1=Label(root,text="Country",width="20",font=("bold",10),fg="blue")
s1.pack()
list1=['Canada','India','UK','Nepal','Iceland','South Africa']
droplist=OptionMenu(root,country,*list1)
droplist.config(width="15")
country.set("Select Country")
droplist.pack()
s3=Label(root,text="messagebox :")
s3.pack()
s2=Button(root,text="Submit",width=20,bg="Brown",fg="White",command=fx)
s2.pack()
s4=Entry(root,width=50,textvariable=z)
s4.pack()




root.mainloop()



from tkinter import *

root=Tk()

root.geometry("700x500")
def calculate():
    Shampoo =e1.get()
    Facewash=e2.get()
    Tea=e3.get()
    Biscuit=e4.get()
    print(type(Tea))
    total=((int(Shampoo)*500)+(int (Facewash)*700)+(int  (Tea)*30)+(int (Biscuit)*200))
    Label12=Label(root, text=total, font="times 18 bold")
    Label12.place(x=100, y=360)

Label6=Label(root,text="Esha's Store",font="times 30 bold ")
Label6.place(x=350,y=20, anchor="center")
#*******menu********

Label1=Label(root,text="Menu",font="times 28 bold ")
Label1.place(x=550,y=70)
Label2=Label(root,text="Shampoo    500tk",font="times 18 bold")
Label2.place(x=450,y=120)
Label3=Label(root,text="Facewash   700tk",font="times 18 bold")
Label3.place(x=450,y=150)
Label4=Label(root,text="     Tea        30tk",font="times 18 bold")
Label4.place(x=450,y=180)
Label5=Label(root,text=" Biscuits     200tk",font="times 18 bold")
Label5.place(x=450,y=210)



#..........billing.....
Label7=Label(root,text="Select the items",font="times 20 bold ")
Label7.place(x=70,y=70)
Label8=Label(root,text="Shampoo",font="times 18 bold ")
Label8.place(x=20,y=120)
e1=Entry(root)
e1.place(x=20,y=150)
Label9=Label(root,text="Facewash",font="times 18 bold ")
Label9.place(x=250,y=120)
e2=Entry(root)
e2.place(x=250,y=150)

Label10=Label(root,text="Tea",font="times 18 bold ")
Label10.place(x=20,y=200)
e3=Entry(root)
e3.place(x=20,y=230)

Label11=Label(root,text="Biscuit",font="times 18 bold ")
Label11.place(x=250,y=200)
e4=Entry(root)
e4.place(x=250,y=230)
b2=Button(root,text='bill',width=20,command=calculate)
b2.place(x=100,y=300)

root.mainloop()
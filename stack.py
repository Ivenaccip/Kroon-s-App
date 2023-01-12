from tkinter import *

top = Tk()
width = top.winfo_screenwidth()
height = top.winfo_screenheight()
top.geometry("%dx%d"  %(width, height))
distance = width/2
L1 = Label(top, text = "Physics")
L1.place(x = distance + 10,y = 10)
E1 = Entry(top, bd = 5, width=50)
E1.place(x = distance +60,y = 10)
L2 = Label(top,text = "Maths")
L2.place(x = distance +10,y = 50)
E2 = Entry(top,bd = 5)
E2.place(x = distance +60,y = 50)

L3 = Label(top,text = "Total")
L3.place(x = distance +10,y = 150)
E3 = Entry(top,bd = 5)
E3.place(x = distance +60,y = 150)

B = Button(top, text = "Add")
B.place(x = distance +100, y = 100)
top.mainloop()
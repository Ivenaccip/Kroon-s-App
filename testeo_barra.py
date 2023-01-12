from tkinter import *

ventana = Tk()
ventana.geometry("400x300")

listbox = Listbox()
listbox.insert(END, *(f"Elemento {i}" for i in range(1, 101)))
listbox.place(x= 10, y=10, width=200, height=180)
scrollbar = Scrollbar(orient=VERTICAL, command=listbox.yview)
listbox.config(
    yscrollcommand=scrollbar.set
)
scrollbar.place(x=220, y = 10, height=180)

ventana.mainloop()
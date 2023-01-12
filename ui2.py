from tkinter import *
"""
class UI_Frames:

    def marco_padre(self, ventana):
        self.ventana = ventana
        width = ventana.winfo_screenwidth()
        print(width)

    marco_padre()
"""

ventana = Tk()
widthPC = ventana.winfo_screenwidth()
heightPC = ventana.winfo_screenheight()
print(f"{widthPC}x{heightPC}")
ventana.geometry("%dx%d" %(widthPC, heightPC))
i = 0
for i in range(3):
    marco_padre = Frame(
        ventana, 
        width=widthPC/3, 
        height=heightPC/3
        )
    marco_padre.config(
        relief= "solid",
        bg = "red",
        bd = 1
        )
    marco_padre.grid(
        row = 0, 
        column= i,
        rowspan=3,
        sticky=NS
        )
    print(i)
    i += 1

ventana.mainloop()
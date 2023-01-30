from tkinter import *

def guardar_input():
    input_value = input_box.get()
    with open("Reparación_botón.txt", "w") as i:
        i.write(input_value)
    warning_ventana.destroy()
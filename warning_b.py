from tkinter import *

def x_item():
    with open("Reparación_botón.txt", "r") as j:
        df = j.read()
        return df

def retorno():
    input_value = input_box.get()
    with open("Reparación_botón.txt", "w") as i:
        i.write(input_value)
    warning_ventana.destroy()

def warning_boton():
    global warning_ventana
    warning_ventana = Tk()
    warning_ventana.title("Warning Botton")
    warning_label = Label(warning_ventana, text="manual repair needed")
    warning_label.pack()
    warning_label = Label(warning_ventana, text="extract the xpath manually")
    warning_label.pack()

    global input_box
    input_box = Entry(warning_ventana)
    input_box.pack()

    next_button = Button(warning_ventana, text="Repaired", command=retorno)
    next_button.pack()

    warning_ventana.mainloop()
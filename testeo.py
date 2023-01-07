import tkinter as tk

# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Checkbuttons y barra de desplazamiento")

# Creamos el diccionario de Checkbuttons
checkbuttons = {
    "Checkbutton 1": tk.BooleanVar(),
    "Checkbutton 2": tk.BooleanVar(),
    "Checkbutton 3": tk.BooleanVar(),
    "Checkbutton 4": tk.BooleanVar(),
    "Checkbutton 5": tk.BooleanVar(),
}

# Creamos la barra de desplazamiento
#scrollbar = tk.Scrollbar(ventana)
#scrollbar.pack(side="right", fill="y")

# Creamos el marco
frame = tk.Frame(ventana)
frame.pack(side="left", fill="both", expand=True)

# Creamos los Checkbuttons
for text, var in checkbuttons.items():
    checkbutton = tk.Checkbutton(frame, text=text, variable=var)
    checkbutton.pack()

# Vinculamos la barra de desplazamiento con el marco
#scrollbar.config(command=frame.yview)
#frame.config(yscrollcommand=scrollbar.set)

# Creamos el botón "Guardar"
def guardar():
    seleccionados = [text for text, var in checkbuttons.items() if var.get()]
    with open("seleccionados.txt", "w") as f:
        f.write("\n".join(seleccionados))

boton_guardar = tk.Button(ventana, text="Guardar", command=guardar)
boton_guardar.pack()

ventana.mainloop()
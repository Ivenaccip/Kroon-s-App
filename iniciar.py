from tkinter import *
import os.path

class Iniciar:
    
    def __init__(self):
        self.title = "Kroon's App"
        self.geometry = "%dx%d"
        self.icono = './imagenes/fav.ico'

    def cargar(self, ventana):
        self.ventana = ventana

        #Expandible
        width = ventana.winfo_screenwidth()
        height = ventana.winfo_screenheight()
        ventana.geometry(self.geometry  %(width, height))
        ventana.title(self.title)

        #Favicon
        ruta_icono = os.path.abspath(self.icono)
        ventana.iconbitmap(ruta_icono)

    def mostrar(self, ventana):
        self.ventana = ventana
        ventana.mainloop()

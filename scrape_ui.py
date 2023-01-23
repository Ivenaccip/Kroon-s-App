from tkinter import *
from log import load
import json

class UI_Scrape:

#Hace falta crear un nuevo frame padre y de este poner hasta abajo el botón
    """  
    def run(self, ventana):

        self.ventana = ventana
        boton_run = Button(ventana, text="RUN!" , command = correr)
        boton_run.grid(row  = 150,column = 1,sticky=S)
        boton_run.config(padx=20)
        """


def correr():
    loging = load()
    with open("links_seleccionados.txt", "r") as h:
        leer = h.read()
    obj_perfiles = json.loads(leer)
    primer_objeto = obj_perfiles[0]
    print(len(obj_perfiles))
    loging.setUp()
    loging.test_instagram(primer_objeto)
    loging.tearDown()


class Scroll:
    
    def scroll(self, ventana):
        self.ventana = ventana
        v_s = Scrollbar(ventana)
        listbox = Listbox(ventana)
        v_s.grid(row=0, column=1, sticky="nsew")
        listbox.grid(row=0, column=0, sticky="nsew", columnspan=2)
        v_s.config(command=listbox.yview)

        num = 0
        i = 1
        for i in range(20):
            checkbtn = Checkbutton(ventana, text=i)
            listbox.insert(num, checkbtn)
            num += 1

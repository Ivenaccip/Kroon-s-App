from tkinter import *
from iniciar import Iniciar
from ui import Seccion
from scrape_ui import UI_Scrape, Scroll

programa = Iniciar()
ui = Seccion()
ui_s = UI_Scrape()
scr = Scroll()
ventana = Tk()
programa.cargar(ventana)
ui.marco(ventana, "Influencers", 0, 0)
ui.marco(ventana, "All Influencers",0, 1)
ui.marco(ventana, "Links",1, 0)
ui.marco(ventana, "All Links",1, 1)
ui.marco(ventana, "Brands",2, 0)
ui.frames(ventana, "All Brands", 2, 1)
#ui.influencer(ventana)
#ui.infl(ventana)
#Corregir 
ui.links_influencer(ventana)
ui.chatgpt3(ventana) 
#Sample
#ui.prefab(ventana, 3, "Shifrajumelet", "https://www.instagram.com/shifrajumelet/?hl=nl")
ui.frames(ventana, "All Influencers", 0,2)
ui.frames(ventana, "All Links", 1,2)
ui_s.run(ventana)
programa.mostrar(ventana)
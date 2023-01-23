import tkinter as tk
from tkinter import ttk
import json
import os
from PIL import ImageTk, Image
from ttkwidgets import CheckboxTreeview
from diccionario_hashtags import *

class TreeviewFrame(ttk.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.vscrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL)
        self.treeview = ttk.Treeview(
            self,
            selectmode="extended",
            yscrollcommand=self.vscrollbar.set
        )
        self.vscrollbar.config(command=self.treeview.yview)
        self.vscrollbar.grid(row = 1, column=2, sticky='ns')
        self.treeview.grid(row = 1, column=0)

def selectItem():
    links_list = []
    names_list = []
    selected_item = treeview_frame.treeview.selection()
    for item in selected_item:
        current_item = treeview_frame.treeview.item(item)
        company = current_item.get("values")[0]
        link = current_item.get("values")[1]
        links_list.append(link)
        names_list.append(company)

    json_str_links = json.dumps(links_list)
    with open("links_seleccionados.txt", "w") as f:
        f.write(json_str_links)
    json_str_names = json.dumps(names_list)
    with open("names_seleccionados.txt", "w") as g:
        g.write(json_str_names)

def checkbuttons(root):
    all_inf = tk.Checkbutton(root, text = "Select All Influencers")
    all_inf.grid(row = 0, column=0)
    all_links = tk.Checkbutton(root, text = "Select All Links")
    all_links.grid(row = 0, column=1)
    all_links = tk.Checkbutton(root, text = "Select All Brands")
    all_links.grid(row = 0, column=3)

root = tk.Tk()
width_s = root.winfo_screenwidth()
height_s = root.winfo_screenheight()
root.geometry("%dx%d"  %(width_s, height_s))
checkbuttons(root)
root.title('Kroons App')
espacio = tk.Frame()
espacio.grid(row = 1, column=1)
treeview_frame = TreeviewFrame()
treeview_frame.grid(row=1, column=0, columnspan=2)
treeview_frame.treeview.config(columns=("name", "ligas"), show="headings")
treeview_frame.treeview.heading("name", text="Influencers")
treeview_frame.treeview.heading("ligas", text="Links")
#treeview brands
tf3 = CheckboxTreeview(root)
tf3.grid(row = 1, column=3)
for key, values in hashtags.items():
    parent = tf3.insert("", "end", key, text = key)
    for value in values:
        tf3.insert(parent, "end", value, text = value)

tf3_scroll = ttk.Scrollbar(orient=tk.VERTICAL)
tf3_scroll.config(command=tf3.yview)
tf3_scroll.grid(row=1, column=4, sticky='ns')

with open("perfiles.txt", "r") as f:
    var = f.read()
objeto = json.loads(var)
for node in objeto:
    treeview_frame.treeview.insert("", tk.END, values=(node, objeto[node]))

#Botón seleccionados
btn_get = tk.Button(root, text="Get data", command=selectItem)
btn_get.grid(row=2, column=1, columnspan= 2)
root.mainloop()